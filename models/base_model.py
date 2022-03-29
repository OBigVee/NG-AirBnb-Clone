#!/usr/bin/python3

import uuid
import datetime
from datetime import date
#from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
    
        self.timeFormat = "&Y-%m-%dT%H:%M:%S.%f"
        self.id:str = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.today()

        from models import storage
        if kwargs != None:
            for k,v in kwargs.items():
                if k == "created_at" | k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, self.timeFormat)
                else:
                    storage.new(self)
        else:
            self.id:str = str(uuid.uuid4())
            self.created_at = datetime.now()


        
    def __str__(self) -> str:
        """Return: str representation of class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    
    def save(self):
        """update the publice instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return dict containing all keys/values of __dict__ of the instance"""
        obj = self.__dict__
        obj["created_at"] = self.created_at.isoformat()
        obj["updated_at"] = self.updated_at.isoformatt()
        obj["__class__"] = self.__class__.__name__
        return obj


