#!/usr/bin/python
"""This module contains the base class for all classes"""
import datetime
from typing import Any
import uuid

class BaseModel:
    """Base class for all models
      
    Attributes:
    id(str): string containing instance uuid
       	created_at(datetime): current datetime when an instance is created
        	updated_at(datetime): current datetime and updated every time object is changed
      """
    id = str(uuid.uuid4)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def save(self):
        """updates updated_at information"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        pass

    def __str__(self):
            return f"{self.__class__.__name__} {self.id} {self.__dict__}"

