from abc import ABC, abstractmethod
from exceptions import InvalidRatingError


class Vehicle(ABC):
    def __init__(self, driver_name, rating):
        self.driver_name = driver_name
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value <1 or value>5:
            raise InvalidRatingError("Rating must be between 1 and 5")
        self._rating = value


    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bike(Vehicle):
    def calculate_fare(self, distance):
        return distance*15


class Car(Vehicle):
    def calculate_fare(self, distance):
        return distance*25

    
