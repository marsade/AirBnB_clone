#!/usr/bin/python3
"""Test cases for the File Storage System"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """Test file storage instantiation"""

    def setUp(self):
        """Set up the class"""
        self.fm1 = FileStorage()

    def tearDown(self):
        """Tear down the class"""
        del self.fm1

    def test_no_args(self):
        """Test with no arguments"""
        self.assertIsInstance(self.fm1, FileStorage)

    def test_objects_is_private_dict(self):
        """Teat if objects is private dict attribute"""
        self.assertIsInstance(self.fm1._FileStorage__objects, dict)

    def test_file_path_is_private_str(self):
        """Test if file path is private string attribute"""
        self.assertIsInstance(self.fm1._FileStorage__file_path, str)


class TestFileStorageMethods(unittest.TestCase):
    """Test FileStorage methods"""

    def setUp(self):
        """Set up the classes used"""
        self.fm = FileStorage()
        self.bm = BaseModel()

    def tearDown(self):
        """Tear down the classes used"""
        del self.fm
        del self.bm

    def test_all_return(self):
        """Test the all methods"""
        self.assertIsInstance(self.fm.all(), dict)

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()
