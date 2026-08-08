"""
Module: sensorkit/base.py
Contributor: Zoe Eyram Tsogbe Glover
Student ID: 59112029
Date: 5th August 2026
Role: Define the abstract Sensor base class that every sensor must follow.

Complete the TODOs below.
"""
from abc import ABC, abstractmethod


class Sensor(ABC):

    def __init__(self, name):
        
        self.name = name


    @abstractmethod
    def read(self, raw):
        """Convert a raw signal value into a calibrated reading."""

        pass

    @abstractmethod
    def units(self):
        """Return this sensor's unit string, e.g. 'C' or 'bar'."""

        pass


    def describe(self):
        print(f"{self.name} sensor, measured in {self.units()}")
