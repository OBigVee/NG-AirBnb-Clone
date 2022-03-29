#!/usr/bin/python3
"""User model"""

from models.base_model import BaseModel
from models import storage

class User(BaseModel):

    #def __init__(self, email:str, password:str, first_name:str, last_name:str)
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    