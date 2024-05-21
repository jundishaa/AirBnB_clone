#!/usr/bin/python3
"""
This module contains the BaseModel class
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initialize the BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of the BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return the dictionary representation of the BaseModel
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
