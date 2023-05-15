#!/usr/bin/python3
"""This is the class City modules"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class inherits from a BaseModel,
    + with the attribute:
    state_id: string - empty string
    name (str): The name of the state.
    """

    name = ""
