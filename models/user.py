#!/usr/bin/python3
"""this class, 'User'inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a user with the following Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
