#!/usr/bin/python3
"""
Class BaseModel
Definitions
"""

from datetime import datetime
import models
from uuid import uuid4

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class Derivitives"""

    def __init__(self, *args, **kwargs):
        """ initialized the base model creayted_id and updated_id"""
        if len(kwargs) != 0:
            for key, item in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    self.created_at = datetime.datetime.strptime(
                        item, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                        item, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, item)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Representation BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Change time current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        containing all keys/values of the instance"""
        dict_class = self.__dict__.copy()
        if "created_at" in dict_class:
            dict_class["created_at"] = dict_class["created_at"].strftime(time)
        if "updated_at" in dict_class:
            dict_class["updated_at"] = dict_class["updated_at"].strftime(time)
        dict_class["__class__"] = self.__class__.__name__
        return dict_class
