#!/usr/bin/python3
"""
Test for storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    def test_all(self):
        """test all method"""
        storage = FileStorage()
        objects = storage.all()
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)

    def test_new(self):
        """test new method"""
        obj = BaseModel()
        self.new(obj)
        objects = storage.all()
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, str(obj.id))
        self.assertEqual(objects[key] is obj, True)
