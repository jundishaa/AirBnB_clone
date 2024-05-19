#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.model = BaseModel()
    
    def test_instance(self):
        """Test instantiation of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
    
    def test_id(self):
        """Test id is a valid uuid"""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(uuid.UUID(self.model.id))
    
    def test_created_at(self):
        """Test created_at is a datetime instance"""
        self.assertIsInstance(self.model.created_at, datetime)
    
    def test_updated_at(self):
        """Test updated_at is a datetime instance"""
        self.assertIsInstance(self.model.updated_at, datetime)
    
    def test_save(self):
        """Test save method updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
    
    def test_to_dict(self):
        """Test to_dict method returns correct dictionary"""
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(obj_dict, dict)

    def test_dict_to_instance(self):
        """Test creating an instance from a dictionary"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        
        my_new_model = BaseModel(**my_model_json)
        
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertNotEqual(my_model, my_new_model)


if __name__ == "__main__":
    unittest.main()
