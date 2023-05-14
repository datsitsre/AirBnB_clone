#!/usr/bin/python3
"""This is the class State modules"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class inherits from a BaseModel,
    + with the attribute:
    name (str): The name of the state.
    """

    name = ""
