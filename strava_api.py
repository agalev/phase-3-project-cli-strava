import requests
import pandas as pd
import api_key
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.classes.models import Profile, Activity, Stats, Achievement, ProfileAchievement

engine = create_engine('sqlite:///strava.db')
Session = sessionmaker(bind=engine)
session = Session()

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"
profile_url = "https://www.strava.com/api/v3/athlete"
payload = {
    'client_id': api_key.client_id,
    'client_secret': api_key.client_secret,
    'refresh_token': api_key.refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}
# Refresh Token
print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))
header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}

# Get Profile from Strava and add to database
def get_profile():
#     session.query(Profile).delete()
#     session.commit()
# get_profile()
  my_profile = requests.get(profile_url, headers=header).json()
  profile_cols = ['username', 'firstname', 'lastname', 'bio',
                  'city', 'state', 'country', 'sex', 'created_at',
                  'weight']
  formatted_profile = [my_profile[col] for col in profile_cols]
  profile = Profile(username = formatted_profile[0],
                    firstname = formatted_profile[1],
                    lastname = formatted_profile[2],
                    bio = formatted_profile[3],
                    city = formatted_profile[4],
                    state = formatted_profile[5],
                    country = formatted_profile[6],
                    sex = formatted_profile[7],
                    created_at = formatted_profile[8],
                    weight = formatted_profile[9]
                    )
  if session.query(Profile).filter_by(username=profile.username).first():
      print("Profile already exists")
  else:
      print("Adding profile to database")
      session.add(profile)
      session.commit()
  
# Get Activities from Strava and add to database
def get_dataset():
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    activity_cols = ['type', 'distance', 'moving_time', 'elapsed_time',
        'total_elevation_gain', 'start_date_local', 'timezone',
        'achievement_count', 'kudos_count', 'comment_count',
        'start_latlng', 'end_latlng', 'average_speed',
        'max_speed', 'average_heartrate', 'max_heartrate',
        'elev_high', 'elev_low', 'pr_count','id'
        ]
    for i in range(len(my_dataset)):
        formatted_activity = []
        for col in activity_cols:
            try:
                formatted_activity.append(my_dataset[i][col])
            except:
                formatted_activity.append(None)
        activity = Activity(type = formatted_activity[0],
                            distance = formatted_activity[1],
                            moving_time = formatted_activity[2],
                            elapsed_time = formatted_activity[3],
                            total_elevation_gain = formatted_activity[4],
                            start_date_local = formatted_activity[5],
                            timezone = formatted_activity[6],
                            achievement_count = formatted_activity[7],
                            kudos_count = formatted_activity[8],
                            comment_count = formatted_activity[9],
                            start_latlng = str(formatted_activity[10]),
                            end_latlng = str(formatted_activity[11]),
                            average_speed = formatted_activity[12],
                            max_speed = formatted_activity[13],
                            average_heartrate = formatted_activity[14],
                            max_heartrate = formatted_activity[15],
                            elev_high = formatted_activity[16],
                            elev_low = formatted_activity[17],
                            pr_count = formatted_activity[18],
                            strava_id = formatted_activity[19],
                            profile_id = 1
                            )
        if session.query(Activity).filter_by(strava_id=activity.strava_id).first():
            print("Activity already exists")
        else:
            print("Adding activity to database")
            session.add(activity)
            session.commit()
    # for activity in my_dataset:
    #     print(activity['type'])
# get_dataset()


# my_stats = requests.get(athlete_stats_url, headers=header).json()


# print(([my_profile[col] for col in profile_cols]))
# profile = Profile([my_profile[col] for col in profile_cols])
# my_profile = "username = 'alexander_galev', firstname = 'Alexander', lastname = 'Galev', bio = 'Mainly rollerblading, some run and bike.', city = 'Denver', state = 'Colorado', country = 'United States', sex = 'M', created_at = '2022-02-23T02:19:26Z', weight = 77.1107"


# stats_cols = ['biggest_ride_distance', 'all_ride_totals',
#               'all_run_totals', 'ytd_ride_totals', 'ytd_run_totals']

# print(my_profile)
# activities = pd.json_normalize(my_dataset[0])
# print(activities[cols])
# print(activities.columns)

# for i in range(len(my_dataset)):
#     print(f'Activity {i}:')
#     for col in activity_cols:
#         try:
#           print(f'\t{col}: {my_dataset[i][col]}')
#         except: print(f'\t{col}: None')

# for i in range(len(my_dataset)):
#     print(f'Activity {i}: \n {my_dataset[i]}')


# for i in my_stats:
#     print(f'{i} : {str(my_stats[i])}')

def scrub():
    session.query(Activity).delete()
    session.commit()
    session.query(Profile).delete()
    session.commit()
    session.query(Stats).delete()
    session.commit()
    session.query(Achievement).delete()
    session.commit()
    session.query(ProfileAchievement).delete()
    session.commit()

def populate():
    get_profile()
    get_dataset()

    
populate()
# scrub()