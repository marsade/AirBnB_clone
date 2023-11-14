#!/usr/bin/python3
"""This module contains the base class for all classes"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize the class instance

        Attributes:
            created_at(datetime): current datetime when an instance is created
            id(str): string containing instance uuid
            updated_at(datetime): current datetime and updated
            every time object is changed
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict representation of the Base object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns a string representation of the object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
