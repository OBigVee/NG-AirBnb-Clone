#!usr/bin/python3
"""Place"""


from models.base_model import BaseModel

class Place(BaseModel):
    city_id:str = ""
    user_id:str = ""
    name:str = ""
    description:str = ""
    number_room:int = 0
    number_bathrooms:int = 0
    max_guest:int = 0
    price_by_nigt:int = 0
    latitude:float = 0.0
    amenity_ids:list = [] 
    
