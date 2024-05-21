#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """File storage engine for persisting BaseModel instances to a JSON file."""

    def __init__(self, file_path):
        """Initialize a FileStorage instance with the given file path.

        Args:
            file_path (str): Path to the JSON file for storage.
        """
        self.__file_path = file_path
        self.__objects = {}
        self.reload()

    def all(self):
        """Return the dictionary of stored objects.

        Returns:
            dict: Dictionary of stored objects with keys as "<class name>.<id>" and values as objects.
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage with the key <class name>.id.

        Args:
            obj (BaseModel): BaseModel instance to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize the stored objects to the JSON file at the specified path."""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserialize the JSON file and store the objects, if it exists.

        If the file does not exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
