#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
if environ['HBNB_TYPE_STORAGE'] == "db":
    cities = relationship("City", back_populates="state")

if environ['HBNB_TYPE_STORAGE'] == "file":
    @property
    def cities(self):
        cities_list = models.storage.all(type(City))
        matching_cities = []
        for i in cities_list:
            if cities_list.get(i).state_id == self.id:
                matching_cities.append(cities_list.get(i))
        return matching_cities
