from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

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

class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer(), primary_key=True)
    total_distance = Column(Integer())
    average_speed = Column(Integer())
    max_speed = Column(Integer())
    average_heartrate = Column(Integer())
    max_heartrate = Column(Integer())
    profile_id = Column(Integer(), ForeignKey('profiles.id'))

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

class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String())
    elapsed_time = Column(Integer())
    distance = Column(Integer())
    average_speed = Column(Integer())
    max_speed = Column(Integer())
    average_heartrate = Column(Integer())
    max_heartrate = Column(Integer())

class ProfileAchievement(Base):
    __tablename__ = 'profile_achievements'

    id = Column(Integer(), primary_key=True)
    profile_id = Column(Integer(), ForeignKey('profiles.id'))
    achievement_id = Column(Integer(), ForeignKey('achievements.id'))
