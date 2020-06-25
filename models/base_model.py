#!/usr/bin/python3
"""Base model class"""
import uuid
import models
from datetime import datetime


Class BaseModel:
""" xxx """
def __str__(self):
    """returns a string of class name, id, and dictionary"""
    return "[{}] ({}) {}".format(
        type(self).__name__, self.id, self.__dict__)