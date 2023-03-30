from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///strava.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    firstname = Column(String())
    lastname = Column(String())
    bio = Column(String())
    city = Column(String())
    state = Column(String())
    country = Column(String())
    sex = Column(String())
    created_at = Column(String())
    weight = Column(Integer())
    last_updated = Column(String(), default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    activities = relationship("Activity", backref=backref("profile"))
    stats = relationship("Stats", backref=backref("profile"))
    profile_achievements = relationship("ProfileAchievement", back_populates="profiles")
    achievements = association_proxy("profile_achievements", "achievements", creator=lambda achievements: ProfileAchievement(achievements=achievements))

    def __repr__(self):
        return f'''
___________________________
| Profile Details
|
| ID: {self.id}
|
| Created At: {self.created_at}
|
| Username: {self.username}
|
| First Name: {self.firstname}
|
| Last Name: {self.lastname}
|
| Gender: {self.sex}
|
| Weight: {int(self.weight)} lbs
|
| Short Bio: {self.bio}
|
| Location: {self.city}, {self.state}, {self.country}
|
| Last Updated from Strava: {self.last_updated}
'''

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer(), primary_key=True)
    strava_id = Column(Integer())
    type = Column(String())
    distance = Column(Integer())
    moving_time = Column(Integer())
    elapsed_time = Column(Integer())
    total_elevation_gain = Column(Integer())
    start_date_local = Column(String())
    timezone = Column(String())
    achievement_count = Column(Integer())
    kudos_count = Column(Integer())
    comment_count = Column(Integer())
    start_latlng = Column(String())
    end_latlng = Column(String())
    average_speed = Column(Integer())
    max_speed = Column(Integer())
    average_heartrate = Column(Integer())
    max_heartrate = Column(Integer())
    elev_high = Column(Integer())
    elev_low = Column(Integer())
    pr_count = Column(Integer())
    profile_id = Column(Integer(), ForeignKey('profiles.id'))

    profile_achievements = relationship("ProfileAchievement", back_populates="activities")

    def __repr__(self):
        return f'''
__________________________
| Activity id: {self.id}'
| Type: {self.type}
| Distance: {int(self.distance * 0.000621371 )} miles
| Moving Time: {int(self.moving_time / 60)} minutes
| Down Time: {int((self.elapsed_time - self.moving_time) / 60)} minutes
| Elapsed Time: {int(self.elapsed_time / 60)} minutes
| Total Elevation Gain: {int(self.total_elevation_gain * 3.28084)} feet
| Start Date: {self.start_date_local}
| Timezone: {self.timezone}
| Achievement Count: {self.achievement_count}
| Kudos Count: {self.kudos_count}
| Comment Count: {self.comment_count}
| Average Speed: {int(self.average_speed * 2.23)} mph
| Max Speed: {round(self.max_speed * 2.23, 2)} mph
| Average Heartrate: {int(self.average_heartrate) if isinstance(self.average_heartrate, int) else 'N/A'} bpm
| Max Heartrate: {self.max_heartrate if isinstance(self.max_heartrate, int) else 'N/A'} bpm
| Elevation High: {int(self.elev_high * 3.28084)} feet
| Elevation Low: {int(self.elev_low * 3.28084)} feet
| PR Count: {self.pr_count}
'''
    
class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer(), primary_key=True)
    type = Column(String())
    total_distance = Column(Integer())
    average_speed = Column(Integer())
    max_speed = Column(Integer())
    average_heartrate = Column(Integer())
    max_heartrate = Column(Integer())
    profile_id = Column(Integer(), ForeignKey('profiles.id'))

    def __repr__(self):
        return f'''
________________________________________________________________________________________________________________________________________________________
| Type: {self.type} | Total Distance: {int(self.total_distance * 0.000621371 )} miles | Average Speed: {int(self.average_speed * 2.23)} mph | Max Speed: {self.max_speed * 2.23} mph | Average Heartrate: {int(self.average_heartrate)} bpm | Max Heartrate: {self.max_heartrate if isinstance(self.max_heartrate, int) else 'N/A'} bpm
'''

class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    type = Column(String())
    elapsed_time = Column(Integer())
    distance = Column(Integer())
    average_speed = Column(Integer())
    max_speed = Column(Integer())
    average_heartrate = Column(Integer())
    max_heartrate = Column(Integer())

    profile_achievements = relationship("ProfileAchievement", back_populates="achievements")
    profile = association_proxy("profile_achievements", "profile", creator=lambda profile: ProfileAchievement(profile=profile))

    def __repr__(self):
        return f'Achievement name: {self.name}'

class ProfileAchievement(Base):
    __tablename__ = 'profile_achievements'

    id = Column(Integer(), primary_key=True)
    profile_id = Column(Integer(), ForeignKey('profiles.id'))
    achievement_id = Column(Integer(), ForeignKey('achievements.id'))
    activity_id = Column(Integer(), ForeignKey('activities.id'))

    profiles = relationship("Profile", back_populates="profile_achievements")
    achievements = relationship("Achievement", back_populates="profile_achievements")
    activities = relationship("Activity", back_populates="profile_achievements")

    def lookup(self, profile_id, achievement_id, activity_id):
        profile = session.query(Profile).filter_by(id=profile_id).first()
        achievement = session.query(Achievement).filter_by(id=achievement_id).first()
        activity = session.query(Activity).filter_by(id=activity_id).first()
        return profile, achievement, activity
    
    def __repr__(self):
        profile, achievement, activity = self.lookup(self.profile_id, self.achievement_id, self.activity_id)    
        return f'''
___________________________________________
| Achievement: {achievement.name}
| Earned on: {activity.start_date_local}
| Actual distance: {round(activity.distance * 0.000621371, 2)} miles | Actual time: {int(activity.elapsed_time / 60)} minutes | Average speed: {round(activity.average_speed * 2.23, 2)} mph | Average heartrate: {int(activity.average_heartrate)} bpm | Max heartrate: {activity.max_heartrate if isinstance(activity.max_heartrate, int) else 'N/A'} bpm
'''