import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    email = Column(String(50), unique = True)
    password = Column(String(25), nullable = False)

class Planet (Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key = True)
    name = Column(String(25))
    population = Column(Integer)
    climate = Column(String(25))
    terrain = Column(String(25))
    gravity = Column(String(25))

class Character (Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String(25))
    birthYear = Column(String(25))
    gender = Column(String(25))
    mass = Column(String(25))
    height = Column(String(25))
    planet = Column(Integer, ForeignKey("planet.id"))
    planet_relationship = relationship(Planet)

class Starship (Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key = True)
    name = Column(String(25))
    manufacturer = Column(String(25))
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)

class Favorite_Planets (Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey = "user.id")
    user_id_relationship = relationship(User)
    planet_id = Column(Integer, ForeignKey = "planet.id")
    planet_id_relationship = relationship(Planet)

class Favorite_Characters (Base):
    __tablename__ = "favorite_characters"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey = "user.id")
    user_id_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey = "character.id")
    character_id_relationship = relationship(Character)

class Favorite_Starships (Base):
    __tablename__ = "favorite_starships"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey = "user.id")
    user_id_relationship = relationship(User)
    starship_id = Column(Integer, ForeignKey = "starship.id")
    starship_id_relationship = relationship(Starship)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
