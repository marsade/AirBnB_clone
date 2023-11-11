#!/usr/bin/python3
"""Unit tests for the Base class"""
import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Unit tests for the Base class"""
    def setUp(self):
        """Set up the class"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self):
        """Tear down the class"""
        del self.bm1
        del self.bm2

    def test_created_at(self):
        """Test created_at method"""
        self.assertTrue(hasattr(self.bm1, 'created_at'))
        self.assertIsInstance(self.bm1.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at method"""
        self.assertTrue(hasattr(self.bm1, 'updated_at'))
        self.assertIsInstance(self.bm1.updated_at, datetime.datetime)

    def test_uuid(self):
        """Test unique uuid"""
        self.assertTrue(hasattr(self.bm1, 'id'))
        self.assertIsInstance(self.bm1.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_to_dict(self):
        """Test to_dict method"""
        new_bm1 = self.bm1.to_dict()
        self.assertIsInstance(new_bm1, dict)
        self.assertIn('__class__', new_bm1)
        self.assertEqual(new_bm1.get('__class__'), 'BaseModel')
