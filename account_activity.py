import requests
import json
import pandas as pd

api_token = $dbt_cloud_api_token
account_id = $account_id

base_url = "https://cloud.getdbt.com/api/v2"
url_groups = "/accounts/" + account_id + "/users/"
headers = {'Authorization': 'Token '+ api_token + ''}

groups_endpoint = base_url + url_groups

r_groups = requests.get(groups_endpoint, headers = headers)

payload_groups = json.loads(r_groups.content)

data_groups=[]

#data.permissions.groups.name
for i in payload_groups['data']:
    for permissions in i['permissions']:
        for groups in permissions['groups']:
            data_groups.append([permissions['account_id'],i['fullname'],i['id'],i['email'],permissions['license_type'],i['last_login'],groups['name']])

df_users_groups = pd.DataFrame(data_groups, columns = ['Account ID','Full Name', 'User ID', 'Email', 'License Type', 'Last Login','Groups']).groupby(['Account ID','Full Name','User ID','Email','License Type','Last Login'], as_index=False)['Groups'].apply(','.join)