#!/usr/bin/python3
"""Unit tests for the Base class"""
import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
      def setUp(self):
            self.bm1 = BaseModel()

      def tearDown(self):
            del self.bm1

      def test_created_at(self):
            self.assertTrue(hasattr(self.bm1, 'created_at'))
            self.assertIsInstance(self.bm1.created_at, datetime.datetime)

      def test_uuid(self):
            pass
      