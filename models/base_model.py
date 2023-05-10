#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        Base Model main 
    """
    def __init__(self):
        """
            The public instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Print some information 
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
            Save method
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Print  show the dict of the object 
        """
        return "{}".format(self.__dict__)
        
