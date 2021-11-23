#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey


class Amenity(BaseModel):
    '''gives the amenities available for a place'''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = Column('''stuff goes in here for relationships''')
