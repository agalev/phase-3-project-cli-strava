from strava_api import *
from achievements import *
from aggregators import *
from lib.classes.models import *

if __name__ == '__main__':
    print('''
     _______.___________..______          ___   ____    ____  ___           ______  __       __  
    /       |           ||   _  \        /   \  \   \  /   / /   \         /      ||  |     |  | 
   |   (----`---|  |----`|  |_)  |      /  ^  \  \   \/   / /  ^  \       |  ,----'|  |     |  | 
    \   \       |  |     |      /      /  /_\  \  \      / /  /_\  \      |  |     |  |     |  | 
.----)   |      |  |     |  |\  \----./  _____  \  \    / /  _____  \     |  `----.|  `----.|  | 
|_______/       |__|     | _| `._____/__/     \__\  \__/ /__/     \__\     \______||_______||__| 
________________________________________________________________________________________________

Welcome to Strava CLI!
Please enter a username from the following list to view their profile:
''')
    in_session = True
    usernames = session.query(Profile.username).all()
    if len(usernames) == 0:
        print('''
_______________________________________________________
| No profiles exist in the database. Fetch from Strava?
''')
        fetch = input('Y/N: ')
        if fetch == 'Y' or fetch == 'y':
            fetch_data()
            print('''
_______________________________________________________
| Data has been fetched from Strava.
''')
        else:
            print('''
_______________________________________________________
| Exiting...
''')
            in_session = False
    for username in usernames:
      print(username[0])
      username = input('Username: ')
      profile = session.query(Profile).filter_by(username=username).first()
    while in_session:
        if profile:
            print(f'''
_______________________________________
| Welcome to {profile.firstname} {profile.lastname}'s profile!
|
| Please enter a number or type the command from the following list to view specific data:
|
| 1. Profile Details
|
| 2. Aggregated Stats
|
| 3. List of Achievements
|
| 4. List of Activities
|
| 5. Fetch New Data
''')
            command = input('Command: ')
            if command == '1' or command == 'Profile':
                print(f'{profile}')
                print('Would you like to edit your profile?')
                edit = input('Y/N: ')
                if edit == 'Y' or edit == 'y':
                    print('''
______________________________________________________
| Please enter the number or type the command from the following list to edit your profile:
|
| 1. Weight
|
| 2. Bio
|
| 3. Location
''')
                    edit_command = input('Command: ')
                    if edit_command == '1' or edit_command == 'Weight':
                        new_weight = input('New Weight: ')
                        profile.weight = new_weight
                        session.commit()
                        print('''
______________________________________________________
| Your weight has been updated.
''')
                    elif edit_command == '2' or edit_command == 'Bio':
                        new_bio = input('New Bio: ')
                        profile.bio = new_bio
                        session.commit()
                        print('''
______________________________________________________
| Your bio has been updated.
''')
                    elif edit_command == '3' or edit_command == 'Location':
                        new_city = input('New City: ')
                        new_state = input('New State: ')
                        new_country = input('New Country: ')
                        profile.city = new_city
                        profile.state = new_state
                        profile.country = new_country
                        session.commit()
                        print('''
______________________________________________________
| Your location has been updated.
''')
                    else:
                        print('''
______________________________________________________
| Sorry, that is not a valid command.
''')
                elif edit == 'N' or edit == 'n':
                    print('''
______________________________________________________
| Returning to main menu.
''')
                else:
                    print('''
______________________________________________________
| Sorry, that is not a valid command.
''')
            elif command == '2' or command == 'Aggregated Stats':
                stats = session.query(Stats).filter_by(profile_id=profile.id).all()
                for stat in stats:
                    print(stat)
            elif command == '3' or command == 'List of Achievements':
                achievements = session.query(ProfileAchievement).filter_by(profile_id=profile.id).all()
                for achievement in achievements:
                    print(achievement)
            elif command == '4' or command == 'List of Activities':
                print('''
__________________________________________________________________________________________________
| Please enter the number or type the command from the following list to view specific activities:
|
| 1. All Activities
|
| 2. Activities by Type
|
| 3. Last 10 Activities
''')
                activity_command = input('Command: ')
                if activity_command == '1' or activity_command == 'All Activities':
                    activities = session.query(Activity).filter_by(profile_id=profile.id).all()
                    for activity in activities:
                        print(activity)
                elif activity_command == '2' or activity_command == 'Activities by Type':
                    print('''
__________________________________________________________________________________________________
| Please enter the number or type the command from the following list to view specific activities:
|
| 1. Ride
|
| 2. Run
|
| 3. Inline Skating
|
| 4. Hike
|
''')
                    activity_type_command = input('Command: ')
                    if activity_type_command == '1' or activity_type_command == 'Ride':
                        activities = session.query(Activity).filter_by(profile_id=profile.id, type='Ride').all()
                        for activity in activities:
                            print(activity)
                    elif activity_type_command == '2' or activity_type_command == 'Run':
                        activities = session.query(Activity).filter_by(profile_id=profile.id, type='Run').all()
                        for activity in activities:
                            print(activity)
                    elif activity_type_command == '3' or activity_type_command == 'Inline Skating':
                        activities = session.query(Activity).filter_by(profile_id=profile.id, type='InlineSkate').all()
                        for activity in activities:
                            print(activity)
                    elif activity_type_command == '4' or activity_type_command == 'Hike':
                        activities = session.query(Activity).filter_by(profile_id=profile.id, type='Hike').all()
                        for activity in activities:
                            print(activity)
                    else:
                        print('''
______________________________________________________
| Sorry, that is not a valid command.
''')
                elif activity_command == '3' or activity_command == 'Last 10 Activities':
                    activities = session.query(Activity).filter_by(profile_id=profile.id).all()
                    for activity in activities[:10]:
                        print(activity)
                else:
                    print('''
______________________________________________________
| Sorry, that is not a valid command.
''')
            elif command == '5' or command == 'Fetch New Data':
                print('''
______________________________________________________
| Fetching new data from Strava...
''')
                fetch_data()
        else:
            in_session = False
            print('''
______________________________________________________
| Sorry, that username does not exist in the database.
| Please try again later.
''')