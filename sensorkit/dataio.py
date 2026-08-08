"""
Module: sensorkit/dataio.py
Contributor: <Zulaiha Mohammed>
Student ID: <68412029>
Date: <08/05/26>
Role: Load raw sensor readings from a text/CSV file, safely.

Uses pathlib for the file path and exceptions to handle problems.
Complete the TODOs below.
"""
from pathlib import Path


def load_readings(filepath):
    """
    Read a file of raw numeric readings, one value per line, and return
    a list of floats.

    Rules:
      - If the file does not exist, raise FileNotFoundError.
      - Ignore blank lines.
      - If a line is not a valid number, skip it and print a short message
        instead of letting the program crash.
    """
  
    path = Path(filepath)
    readings = []
    try:
        with open (path, 'r') as file:
            content=file.readlines()
        for line in content:
           try:
               line=line.strip()
               line=float(line)
               readings.append(line)
           except ValueError:
               print("Skipping invalid line: 'not_a_number'")
               continue

    except FileNotFoundError:
        print('File does not exist')

    return readings

#print(load_readings('readings.csv'))
                    
