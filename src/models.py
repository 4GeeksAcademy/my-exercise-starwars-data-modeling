import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    favorites = Column(String)
    password = Column(String)  

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(String)
    weight = Column(String)
    mass = Column(String)
    films = Column(String)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    created = Column(String)
    crew = Column(Integer)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String)
    diameter = Column(String)
    gravity = Column(String)
    name = Column(String)

class Favorites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    id_user_favourite = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
