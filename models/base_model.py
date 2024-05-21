#!/usr/bin/python3
import datetime
import uuid


class BaseModel:
    """Base model for all other models in the AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance.

        If kwargs is not empty, set attributes based on the key-value pairs.
        If 'created_at' and 'updated_at' are provided as strings, convert them to datetime objects.
        Otherwise, generate a unique ID and set 'created_at' and 'updated_at' to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at":
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                if key == "updated_at":
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """Update the 'updated_at' attribute to the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Convert the instance to a dictionary representation.

        Include the class name, and convert 'created_at' and 'updated_at' to ISO format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__)
        )
