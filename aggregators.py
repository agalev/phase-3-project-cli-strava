from pandas import DataFrame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.classes.models import Stats, Activity

engine = create_engine('sqlite:///strava.db')
Session = sessionmaker(bind=engine)
session = Session()

def aggregate_stats():
    # Get all activities from database
    activities = session.query(Activity).all()
    # Create empty list for each type to store aggregate stats
    agg_stats_InlineSkate = []
    agg_stats_Run = []
    agg_stats_Ride = []
    agg_stats_Hike = []
    # Loop through activities and aggregate stats
    for activity in activities:
        if activity.type == 'InlineSkate':
            agg_stats_InlineSkate.append([activity.distance, activity.average_speed, activity.max_speed, activity.average_heartrate, activity.max_heartrate])
        elif activity.type == 'Run':
            agg_stats_Run.append([activity.distance, activity.average_speed, activity.max_speed, activity.average_heartrate, activity.max_heartrate])
        elif activity.type == 'Ride':
            agg_stats_Ride.append([activity.distance, activity.average_speed, activity.max_speed, activity.average_heartrate, activity.max_heartrate])
        elif activity.type == 'Hike':
            agg_stats_Hike.append([activity.distance, activity.average_speed, activity.max_speed, activity.average_heartrate, activity.max_heartrate])
        else:
            print('Error: Activity type not accounted for')
    # Create DataFrame from list of aggregate stats
    agg_stats_df_InlineSkate = DataFrame(agg_stats_InlineSkate, columns=['distance', 'average_speed', 'max_speed', 'average_heartrate', 'max_heartrate'])
    agg_stats_df_Run = DataFrame(agg_stats_Run, columns=['distance', 'average_speed', 'max_speed', 'average_heartrate', 'max_heartrate'])
    agg_stats_df_Ride = DataFrame(agg_stats_Ride, columns=['distance', 'average_speed', 'max_speed', 'average_heartrate', 'max_heartrate'])
    agg_stats_df_Hike = DataFrame(agg_stats_Hike, columns=['distance', 'average_speed', 'max_speed', 'average_heartrate', 'max_heartrate'])
    # Create Stats object
    if session.query(Stats).filter(Stats.type == 'InlineSkate').first():
        pass
    else:
        inline_skate_stats = Stats(type = 'InlineSkate',
                                total_distance = agg_stats_df_InlineSkate['distance'].sum(),
                                average_speed = agg_stats_df_InlineSkate['average_speed'].mean(),
                                max_speed = agg_stats_df_InlineSkate['max_speed'].max(),
                                average_heartrate = agg_stats_df_InlineSkate['average_heartrate'].mean(),
                                max_heartrate = agg_stats_df_InlineSkate['max_heartrate'].max(),
                                profile_id = 1
                                )
        
        session.add(inline_skate_stats)
        session.commit()
    if session.query(Stats).filter(Stats.type == 'Run').first():
        pass
    else:
        run_stats = Stats(type = 'Run',
                        total_distance = agg_stats_df_Run['distance'].sum(),
                        average_speed = agg_stats_df_Run['average_speed'].mean(),
                        max_speed = agg_stats_df_Run['max_speed'].max(),
                        average_heartrate = agg_stats_df_Run['average_heartrate'].mean(),
                        max_heartrate = agg_stats_df_Run['max_heartrate'].max(),
                        profile_id = 1
                        )      
        session.add(run_stats)
        session.commit()
    if session.query(Stats).filter(Stats.type == 'Ride').first():
        pass
    else:
        ride_stats = Stats(type = 'Ride',
                        total_distance = agg_stats_df_Ride['distance'].sum(),
                        average_speed = agg_stats_df_Ride['average_speed'].mean(),
                        max_speed = agg_stats_df_Ride['max_speed'].max(),
                        average_heartrate = agg_stats_df_Ride['average_heartrate'].mean(),
                        max_heartrate = agg_stats_df_Ride['max_heartrate'].max(),
                        profile_id = 1
                        )
        session.add(ride_stats)
        session.commit()
    if session.query(Stats).filter(Stats.type == 'Hike').first():
        pass
    else:
        hike_stats = Stats(type = 'Hike',
                        total_distance = agg_stats_df_Hike['distance'].sum(),
                        average_speed = agg_stats_df_Hike['average_speed'].mean(),
                        max_speed = agg_stats_df_Hike['max_speed'].max(),
                        average_heartrate = agg_stats_df_Hike['average_heartrate'].mean(),
                        max_heartrate = agg_stats_df_Hike['max_heartrate'].max(),
                        profile_id = 1
                        )
        session.add(hike_stats)
        session.commit()