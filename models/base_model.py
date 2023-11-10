#!/usr/bin/python3
"""This module contains the base class for all classes"""
import datetime
import uuid

class BaseModel:
    """Base class for all models
      
    Attributes:
        id(str): string containing instance uuid
        created_at(datetime): current datetime when an instance is created
        updated_at(datetime): current datetime and updated every time object is changed
    """
    def __init__(self):
        """Initialize the class instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """updates updated_at information"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict representation of the Base object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
