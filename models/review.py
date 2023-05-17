#!/usr/bin/python3
"""This is the class Review modules"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class inherits from a BaseModel,
    + the attribute:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    name = ""
