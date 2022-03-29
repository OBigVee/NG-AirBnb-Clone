#!usr/bin/python3
"""Review"""


from models.base_model import BaseModel

class Review(BaseModel):
    place_id:str = ""
    user_id:str = ""
    text:str = ""