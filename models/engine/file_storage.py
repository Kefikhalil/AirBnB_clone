#!/usr/bin/python3
''' FileStorage module'''
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
import json
from os import path


class FileStorage():
    ''' serializes instances to a JSON file
    and deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    instances = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City, "Amenity": Amenity,
        "Place": Place,
        "Review": Review}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        my_id = obj.id
        my_cls = obj.__class__.__name__
        my_key = my_cls + "." + my_id
        FileStorage.__objects[my_key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        my_dict = {}
        with open(FileStorage.__file_path, "w") as ff:
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, ff)

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
         If the file doesn’t exist, no exception should be raised)'''
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as xk:
                o = json.load(xk)
                mydict = {}
                for key, value in o.items():
                    mydict[key] = self.instances[value["__class__"]](**value)
                FileStorage.__objects = mydict
        else:
            return
