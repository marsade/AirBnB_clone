#!/usr/bin/python3
"""File Storage System"""
import json
import models.base_model


class FileStorage(models.base_model.BaseModel):
    """File Storage System Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the objects dictionary"""
        key = "{}{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON path"""
        serialized_obj = self.__objects
        json_obj = {}
        for key, obj in serialized_obj.items():
            print("Serial{} key{}".format(key, obj))
        print(json_obj)
        print("Hi")
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """Deserializes and Reloads objects to the objects dict"""
        try:
            with open(self.__file_path, 'r') as file:
                deserialized = json.load(file)
            for key, value in deserialized.items():
                class_name, obj_id = key.split('.')
                class_type = globals().get(class_name)
                self.new(class_type(**value))
        except FileNotFoundError:
            pass
