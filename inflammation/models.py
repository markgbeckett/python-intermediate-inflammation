"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param: 2D array of data
    :returns: vector of arithmetic means of data"""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param: 2D array of data
    :returns: vector of maximum of data"""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param: 2D array of data
    :returns: vector of min of data"""
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max_val = np.max(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_val[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


class Observation:
    """
    A class associated with patient observations (day,value pairs)
    """
    def __init__(self, day, value):
        """
        :param day: day of observation (integer)
        :param value: value of inflammation on that day
        """
        self.day = day
        self.value = value

    def __str__(self):
        """Prints the inflammation value by default"""
        return self.value


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study.

    Requires a patient name on instantiation.
    """
    def __init__(self, name, observations=None):
        """
        :param name: Name of Patient (e.g. Alice)
        :param observations: list of day,value pairs (defalut=None)
        """
        super().__init__(name)

        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        """
        Adds a day,value pair (an observations) to a patient's records.

        :param value: value of inflammation
        :param observations: day value was recorded (corresponds to column)
        """
        
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(value, day)

        self.observations.append(new_observation)
        return new_observation

    @property
    def last_observation(self):
        """Returns the final observation in the set of them."""
        return self.observations[-1]


# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
