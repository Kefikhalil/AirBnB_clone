#!/usr/bin/python3
"""class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review
    Args:
    class inherited by Review
    """
    place_id = ""
    user_id = ""
    text = ""
