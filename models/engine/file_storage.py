#!/usr/bin/python3
"""
defines class filestorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Object serialization (making it a json string)
        Saving the serialized object info to a json file
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                dict_obj = json.load(f)
            for key, value in dict_obj.items():
                self.__objects[key] = eval(key.split(".")[0])(**value)
        except FileNotFoundError:
            pass
