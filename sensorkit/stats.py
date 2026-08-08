"""
Module: sensorkit/stats.py
Contributor: Adwoa Aboagyewaa Afram
Student ID: 96192029
Date: Wednesday 5th August, 2026
Role: Simple summary statistics for a list of numeric readings.

Complete the TODOs below.
"""


def mean(values):
    # TODO : if values is empty, raise ValueError("mean() needs values")
    # TODO : return the average (sum of values divided by how many there are)
    if not values:
        raise ValueError("mean() needs values")
    return sum(values) / len(values)


def minimum(values):
    # TODO: return the smallest value. Hint: the built-in min()
    return min(values)


def maximum(values):
    # TODO: return the largest value. Hint: the built-in max()
    return max(values)


def spread(values):
    # TODO: return maximum(values) - minimum(values)
    return max(values) - min(values)
