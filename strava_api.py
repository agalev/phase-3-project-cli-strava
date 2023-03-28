import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
# from pandas.io.json import json_normalize
import api_key

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': api_key.client_id,
    'client_secret': api_key.client_secret,
    'refresh_token': api_key.refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

# cols = ['name', 'distance', 'total_elevation_gain', 'average_speed', 'max_speed', 'start_date', 'kudos_count', 'location_state']
cols = ['type', 'moving_time', 'elapsed_time', 'start_date']
activities = pd.json_normalize(my_dataset)
print(activities[cols])
# print(activities.columns)

# for i in my_dataset:
#     print(i['start_date'])

# print(my_dataset[0]["map"]["summary_polyline"])