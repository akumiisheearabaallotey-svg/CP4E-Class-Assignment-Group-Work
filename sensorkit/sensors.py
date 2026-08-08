"""
Module: sensorkit/sensors.py
Contributor: Annan Nina Ewurama Kwentsiwa
Student ID: 81592029
Date: 5th August 2026
Role: Provide concrete sensor classes built on the Sensor base class.

Each class must implement both abstract methods: read() and units().
Complete the TODOs below.
"""
from .base import Sensor


class Thermocouple(Sensor):
    def read(self, raw):
        return raw * 24.9 - 0.4

    def units(self):
        return 'C'

class PressureGauge(Sensor):
    def read(self, raw):
        return raw * 2.5
     
    def units(self):
        return 'bar'

class StrainGauge(Sensor):
    def read(self,raw):
        return raw*1000
    
    def units(self):
        return 'microstrain'
