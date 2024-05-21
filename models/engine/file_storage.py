#!/usr/bin/python3
"""This module contains the FileStorage class."""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """This method deserializes the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {k: BaseModel(**v) for k, v in json.load(f).items()}
