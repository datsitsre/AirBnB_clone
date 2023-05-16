#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
import json


class BaseModel:
    """
        Base Model main
    """
    def __init__(self, *args, **kwargs):
        """
            The public instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
            Save method update the updated_at attributes
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Print  show the dict of the object
        """
        base_dic = {}
        base_dic = self.__dict__.copy()
        if "created_at" in base_dic:
            base_dic["created_at"] = self.created_at.isoformat()
        if "updated_at" in base_dic:
            base_dic["updated_at"] = self.updated_at.isoformat()
        base_dic["__class__"] = self.__class__.__name__
        return base_dic

    def __str__(self):
        """
            Print some information
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
