from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///strava.db')

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
        return f'Profile username: {self.username}'

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
        return f'Activity id: {self.id}'
    
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
