from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.classes.models import Achievement, ProfileAchievement, Activity

engine = create_engine('sqlite:///strava.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_achievements():
    run10k = Achievement(name = 'Run 10k',
                        description = 'Run 10k',
                        type = 'Run',
                        distance = 10000,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    run10m = Achievement(name = 'Run 10 miles',
                        description = 'Run 10 miles',
                        type = 'Run',
                        distance = 16093.4,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    runHalfMarathon = Achievement(name = 'Run a half marathon',
                        description = 'Run a half marathon',
                        type = 'Run',
                        distance = 21097.5,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    runMarathon = Achievement(name = 'Run a marathon',
                        description = 'Run a marathon',
                        type = 'Run',
                        distance = 42195,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    inlineSkate10k = Achievement(name = 'Inline skate 10k',
                        description = 'Inline skate 10k',
                        type = 'InlineSkate',
                        distance = 10000,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    inlineSkate10m = Achievement(name = 'Inline skate 10 miles',
                        description = 'Inline skate 10 miles',
                        type = 'InlineSkate',
                        distance = 16093.4,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    inlineSkateHalfMarathon = Achievement(name = 'Inline skate a half marathon',
                        description = 'Inline skate a half marathon',
                        type = 'InlineSkate',
                        distance = 21097.5,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    inlineSkateMarathon = Achievement(name = 'Inline skate a marathon',
                        description = 'Inline skate a marathon',
                        type = 'InlineSkate',
                        distance = 42195,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    bike10k = Achievement(name = 'Bike 10k',
                        description = 'Bike 10k',
                        type = 'Ride',
                        distance = 10000,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    bike10m = Achievement(name = 'Bike 10 miles',
                        description = 'Bike 10 miles',
                        type = 'Ride',
                        distance = 16093.4,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    bikeHalfMarathon = Achievement(name = 'Bike a half marathon',
                        description = 'Bike a half marathon',
                        type = 'Ride',
                        distance = 21097.5,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    bikeMarathon = Achievement(name = 'Bike a marathon',
                        description = 'Bike a marathon',
                        type = 'Ride',
                        distance = 42195,
                        average_speed = 0,
                        max_speed = 0,
                        average_heartrate = 0,
                        max_heartrate = 0,
                        )
    session.add(run10k)
    session.add(run10m)
    session.add(runHalfMarathon)
    session.add(runMarathon)
    session.add(inlineSkate10k)
    session.add(inlineSkate10m)
    session.add(inlineSkateHalfMarathon)
    session.add(inlineSkateMarathon)
    session.add(bike10k)
    session.add(bike10m)
    session.add(bikeHalfMarathon)
    session.add(bikeMarathon)
    session.commit()
# seed_achievements()


def profile_achievements():
    # session.query(ProfileAchievement).delete()
    # session.commit()
    achievements = session.query(Achievement).all()
    activities = session.query(Activity).order_by(Activity.strava_id.asc()).all()
    for activity in activities:
        for achievement in achievements:
            query_profile_achievement = session.query(ProfileAchievement).filter_by(achievement_id = achievement.id, profile_id = activity.profile_id).first()
            if query_profile_achievement:
                continue
            elif achievement.type == activity.type and achievement.distance <= activity.distance:
                profile_achievement = ProfileAchievement(achievement_id = achievement.id,
                                                        profile_id = activity.profile_id,
                                                        activity_id = activity.id
                                                        )
                session.add(profile_achievement)
                session.commit()
profile_achievements()