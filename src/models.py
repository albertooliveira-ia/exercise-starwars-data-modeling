import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)
    
    favorites = relationship('Favorite', backref='user', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))
    height = Column(String(20))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    
    favorited_by = relationship('Favorite', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(String(50))
    diameter = Column(String(50))
    orbital_period = Column(String(50))
    
    favorited_by = relationship('Favorite', backref='planet', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! El archivo diagram.png de Star Wars ha sido generado correctamente.")
except Exception as e:
    print("Hubo un problema generando el diagrama")
    raise e