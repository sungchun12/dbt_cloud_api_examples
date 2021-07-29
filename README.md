# dbt_cloud_api_examples

This repo is a hub for API examples that'll help you programmatically interact with dbt Cloud!

```bash
# setup a venv
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

```

```bash
# create environment variables related to your dbt Cloud account
# in a .env file, example below

# You can find this token in your dbt Cloud profile or Account Settings
DBT_CLOUD_API_TOKEN=<your dbt Cloud api key/token>

# https://cloud.getdbt.com/#/accounts/16173/projects/26588/dashboard/
# you can find this number in the cloud.getdbt.com url
ACCOUNT_ID=<account id>

```

## How to Run

```bash
# prints account and user activity in a snapshot to terminal output
# exports csv and json local files to persist results
python3 account_activity.py
```
