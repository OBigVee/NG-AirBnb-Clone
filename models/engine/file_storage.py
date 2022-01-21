#!/usr/bin/python3

"""FileStorage class serializes instances to a JSON file and deserializes JSON file to instances"""
import json 
from models.base_model import BaseModel
class FileStorage:
    """
    Performs serialization and deserialization functionarity.

    Attributes:
      __file_path(str): path to the json file to store objects
      __objects(dict): dictionary containing all objects
    """
    #__file_path:str = "/file.json"
    #__objects:dict = {}
    def __init__(self):#, file_path, objects):
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        """return the dict __objects"""
        return self.__objects


    def new(self,obj):
        """sets in __objects the  obj with key <obj class name>.id"""
        self.__objects[obj.id] = obj


    def save(self):
        """ serializes __objects to the JSON file (path:__file_path) """
        obj_dict = {obj : self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, "w") as file_obj:
            json.dump(obj_dict, file_obj)


    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path)) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)"""

        # try:
        #     with open(self.__file_path) as file_obj:
        #         obj_dict = json.load(file_obj)
        #         for  obj in obj_dict.values():
        #             cls_name = o["__class__"]
        #             del obj["__class__"]
        #             self.new(eval(cls_name)(**obj))
        # except FileNotFoundError:
        #     return 
        if self.__file_path != "":
            with open(self.__file_path) as file_obj:
                obj_dict = json.load(file_obj)


