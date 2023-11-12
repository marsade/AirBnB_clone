#!/usr/bin/python3
"""File Storage System"""
from models.base_model import BaseModel
import json


class FileStorage(BaseModel):
    """File Storage System Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.objects

    def new(self, obj):
        """Add a new object to the objects dictionary"""
        key = "{}{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON path"""
        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialized_obj, self.__file_path)

    def reload(self):
        """Deserializes and Reloads objects to the objects dict"""
        try:
            with open(self.__file_path, 'r') as file:
                deserialized = json.load(file)
            for key, value in deserialized.items():
                class_name, obj_id = key.split('.')
                class_type = globals().get(class_name)
                self.__objects[key] = class_type(**value)
        except FileNotFoundError:
            pass
