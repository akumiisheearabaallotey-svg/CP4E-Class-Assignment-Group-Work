"""
Module: sensorkit/report.py
Contributor: Aku-Miishee Araba Allotey
Student ID: 95192029
Date: 5/08/2026
Role: Produce a printed summary of calibrated readings for one sensor.

This module ties together a sensor (from sensors.py) and the statistics
functions (from stats.py). Complete the TODOs below.
"""
from .stats import mean, minimum, maximum, spread
from .sensors import Sensor


def summarise(sensor, raw_readings):
    """
    Given a sensor object and a list of raw readings:
      1. Calibrate every raw reading using sensor.read(...)
      2. Print a short summary using the stats functions.
    """

    calibrated = [sensor.read(r) for r in raw_readings]
    u=sensor.units()
    print(f"""
    Report for {sensor.name}
      count:  {len(calibrated)}
      mean:  {mean(calibrated):.2f} {u}
      min:  {minimum(calibrated):.2f} {u}
      max:  {maximum(calibrated):.2f} {u}
      spread: {spread(calibrated):.2f} {u}
    """)
