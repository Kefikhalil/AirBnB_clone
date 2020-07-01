#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User
    Args:
    class inherited by User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
