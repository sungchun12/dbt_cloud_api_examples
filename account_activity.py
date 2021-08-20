import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# capture the secret environment variables from .env file
DBT_CLOUD_API_TOKEN = os.getenv("DBT_CLOUD_API_TOKEN")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")

# construct the api endpoints and headers
base_url = "https://cloud.getdbt.com/api/v2"
url_groups = "/accounts/" + ACCOUNT_ID + "/users/"
headers = {"Authorization": "Token " + DBT_CLOUD_API_TOKEN + ""}

groups_endpoint = base_url + url_groups

r_groups = requests.get(groups_endpoint, headers=headers)

payload_groups = json.loads(r_groups.content)

data_groups = []

# data.permissions.groups.name
for i in payload_groups["data"]:
    for permissions in i["permissions"]:
        for groups in permissions["groups"]:
            data_groups.append(
                [
                    permissions["account_id"],
                    i["fullname"],
                    i["id"],
                    i["email"],
                    permissions["license_type"],
                    i["last_login"],
                    groups["name"],
                    str(groups["sso_mapping_groups"])
                ]
            )

df_users_groups = (
    pd.DataFrame(
        data_groups,
        columns=[
            "Account ID",
            "Full Name",
            "User ID",
            "Email",
            "License Type",
            "Last Login",
            "Groups",
            "SSO Mapping Groups",
        ],
    )
    .groupby(
        ["Account ID", "Full Name", "User ID", "Email", "License Type", "Last Login","SSO Mapping Groups"],
        as_index=False,
    )["Groups"]
    .apply(",".join)
)
print(df_users_groups)

# export dataframe as LOCAL csv
df_users_groups.to_csv("account_activity_snapshot.csv", sep=",", encoding="utf-8")

# export dataframe to LOCAL json file
df_users_groups_json = df_users_groups.to_json(orient="records")

# TODO: add functionality to export to cloud storage bucket

with open("account_activity_snapshot.json", "w") as f:
    f.write(df_users_groups_json)

# export full json payload from the API
with open("payload_groups.json", "w") as f:
    f.write(str(payload_groups))
