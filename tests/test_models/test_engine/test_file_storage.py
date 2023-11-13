#!/usr/bin/python3
"""Test cases for the File Storage System"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """Test file storage instantiation"""

    def setUp(self):
        self.fm1 = FileStorage()

    def tearDown(self):
        del self.fm1

    def test_no_args(self):
        self.assertIsInstance(self.fm1, FileStorage)

    def test_objects_is_private_dict(self):
        self.assertIsInstance(self.fm1._FileStorage__objects, dict)

    def test_file_path_is_private_str(self):
        self.assertIsInstance(self.fm1._FileStorage__file_path, str)


class TestFileStorageMethods(unittest.TestCase):
    """Test FileStorage methods"""

    def setUp(self):
        self.fm = FileStorage()
        self.bm = BaseModel()

    def tearDown(self):
        del self.fm
        del self.bm

    def test_all_return(self):
        self.assertIsInstance(self.fm.all(), dict)

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()
