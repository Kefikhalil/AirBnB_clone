#!/usr/bin/python3
"""Base model class"""
import uuid
import models
from datetime import datetime


class BaseModel():
    """ class base model """
    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args : won't be used.
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """

        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """returns a string of class name, id, and dictionary"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class
        Return:
            return a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
