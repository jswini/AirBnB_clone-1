#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.__init__ import storage
from city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        cities_list = storage.all(type(City))
        matching_cities = []
        for i in cities_list:
            if cities_list.get(i).state_id == self.id:
                matching_cities.append(cities_list.get(i))
        return matching_cities
