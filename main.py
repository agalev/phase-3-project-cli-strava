from strava_api import *
from achievements import *
from aggregators import *
from lib.classes.models import *

if __name__ == '__main__':
    print('''\u001b[33;1m
     _______.___________..______          ___   ____    ____  ___           ______  __       __  
    /       |           ||   _  \        /   \  \   \  /   / /   \         /      ||  |     |  | 
   |   (----`---|  |----`|  |_)  |      /  ^  \  \   \/   / /  ^  \       |  ,----'|  |     |  | 
    \   \       |  |     |      /      /  /_\  \  \      / /  /_\  \      |  |     |  |     |  | 
.----)   |      |  |     |  |\  \----./  _____  \  \    / /  _____  \     |  `----.|  `----.|  | 
|_______/       |__|     | _| `._____/__/     \__\  \__/ /__/     \__\     \______||_______||__| 
________________________________________________________________________________________________
\u001b[0m
\u001b[37;1mWelcome to Strava CLI!
Please enter a your username from the following list to view your profile:\u001b[0m
''')
    in_session = True
    usernames = session.query(Profile.username).all()
    if len(usernames) == 0:
        print('''
_______________________________________________________
| \u001b[31;1mNo profiles exist in the database. Fetch from Strava?\u001b[0m
''')
        fetch = input('Y/N: ')
        if fetch == 'Y' or fetch == 'y':
            fetch_data()
            print('''
_________________________________________________
| \u001b[32;1mData has been fetched from Strava. Restart App.\u001b[0m
''')
        else:
            print('''
____________
| \u001b[31;1mExiting...\u001b[0m
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
| \u001b[7m Logged in as: {profile.username} \u001b[0m
|
| \u001b[7m Welcome to your profile {profile.firstname}! \u001b[0m
|
| \u001b[7m Please enter a number or type the command from the menu: \u001b[0m
|
| \u001b[33;1m1. Profile Details\u001b[0m
|
| \u001b[34;1m2. Aggregated Stats\u001b[0m
|
| \u001b[35;1m3. List of Achievements\u001b[0m
|
| \u001b[36;1m4. List of Activities\u001b[0m
|
| \u001b[32;1m5. Fetch New Data From Strava? (Last Updated: {profile.last_updated})\u001b[0m
|
| \u001b[31;1m6. Logout\u001b[0m
''')
            command = input('Command: ')
            if command == '1' or command == 'Profile':
                print(f'{profile}')
                print('\u001b[7m Would you like to edit your profile? \u001b[0m')
                edit = input('Y/N: ')
                if edit == 'Y' or edit == 'y':
                    print('''
______________________________________________________
| \u001b[7m Please enter the number or type the command from the following list to edit your profile: \u001b[0m
|
| \u001b[33;1m1. Weight\u001b[0m
|
| \u001b[33;1m2. Bio\u001b[0m
|
| \u001b[33;1m3. Location\u001b[0m
''')
                    edit_command = input('Command: ')
                    if edit_command == '1' or edit_command == 'Weight':
                        new_weight = input('New Weight: ')
                        profile.weight = new_weight
                        session.commit()
                        print('''
______________________________________________________
| \u001b[33;1mYour weight has been updated.\u001b[0m
''')
                    elif edit_command == '2' or edit_command == 'Bio':
                        new_bio = input('New Bio: ')
                        profile.bio = new_bio
                        session.commit()
                        print('''
______________________________________________________
| \u001b[33;1mYour bio has been updated.\u001b[0m
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
| \u001b[33;1mYour location has been updated.\u001b[0m
''')
                    else:
                        print('''
______________________________________________________
| \u001b[33;1mSorry, that is not a valid command.\u001b[0m
''')
                elif edit == 'N' or edit == 'n':
                    print('''
______________________________________________________
| \u001b[33;1mReturning to main menu.\u001b[0m
''')
                else:
                    print('''
______________________________________________________
| \u001b[33;1mSorry, that is not a valid command.\u001b[0m
''')
            elif command == '2' or command == 'Aggregated Stats':
                stats = session.query(Stats).filter_by(profile_id=profile.id).all()
                for stat in stats:
                    print(stat)
            elif command == '3' or command == 'List of Achievements':
                print('''
____________________________________________________________________________________________________
| \u001b[7m Please enter the number or type the command from the following list to view specific achievements: \u001b[0m
|
| \u001b[35;1m1. All Achievements\u001b[0m
|
| \u001b[35;1m2. Achievements Earned\u001b[0m
''')
                achievement_command = input('Command: ')
                if achievement_command == '1' or achievement_command == 'All Achievements':
                    achievements = session.query(Achievement).all()
                    for achievement in achievements:
                        print(achievement)
                elif achievement_command == '2' or achievement_command == 'Achievements Earned':
                    achievements = session.query(ProfileAchievement).filter_by(profile_id=profile.id).all()
                    for achievement in achievements:
                        print(achievement)
                else:
                    print('''
_____________________________________
| \u001b[35;1mSorry, that is not a valid command.\u001b[0m
''')
            elif command == '4' or command == 'List of Activities':
                print('''
__________________________________________________________________________________________________
| \u001b[7m Please enter the number or type the command from the following list to view specific activities: \u001b[0m
|
| \u001b[36;1m1. All Activities\u001b[0m
|
| \u001b[36;1m2. Activities by Type\u001b[0m
|
| \u001b[36;1m3. Last 10 Activities\u001b[0m
''')
                activity_command = input('Command: ')
                if activity_command == '1' or activity_command == 'All Activities':
                    activities = session.query(Activity).filter_by(profile_id=profile.id).all()
                    for activity in activities:
                        print(activity)
                elif activity_command == '2' or activity_command == 'Activities by Type':
                    print('''
__________________________________________________________________________________________________
| \u001b[7m Please enter the number or type the command from the following list to view specific activities: \u001b[0m
|
| \u001b[36;1m1. Ride\u001b[0m
|
| \u001b[36;1m2. Run\u001b[0m
|
| \u001b[36;1m3. Inline Skating\u001b[0m
|
| \u001b[36;1m4. Hike\u001b[0m
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
| \u001b[7m Sorry, that is not a valid command. \u001b[0m
''')
                elif activity_command == '3' or activity_command == 'Last 10 Activities':
                    activities = session.query(Activity).filter_by(profile_id=profile.id).all()
                    for activity in activities[:10]:
                        print(activity)
                else:
                    print('''
______________________________________________________
| \u001b[7m Sorry, that is not a valid command. \u001b[0m
''')
            elif command == '5' or command == 'Fetch New Data':
                print('''
______________________________________________________
| \u001b[32;1mFetching new data from Strava...\u001b[0m
''')
                fetch_data()
                print('''
_______________________________________________________
| \u001b[32;1mData has been fetched from Strava. Restart App.\u001b[0m
''')
                in_session = False
            elif command == '6' or command == 'Logout':
                print('''
______________________________________
| \u001b[31;1mLogging out...\u001b[0m
''')
                in_session = False
        else:
            in_session = False
            print('''
______________________________________________________________________________________________
| \u001b[31;1mSorry, that username does not exist in the database. Please try again later.\u001b[0m
''')