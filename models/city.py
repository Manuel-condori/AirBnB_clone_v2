#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """class state inherith from Base"""
    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        places = relationship("Place", cascade="all, delete", backref="cities")

    else:
        name = ""
        state_id = ""
