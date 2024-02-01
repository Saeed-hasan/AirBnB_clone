#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place

"""
model to covert dict to a json and store in file
"""


class FileStorage:
    """
    that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
    __file_path: private attribute that have the path of the json file
    __objects: private attribute that contain the dic of instance
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        This method adds a new object to the
        __objects dictionary. The object is stored
        with a key in the format "<class_name>.<object_id>"
        """
    class_name = obj.__class__.__name__
    key = "{}.{}".format(class_name, str(obj.id))
    self.__objects[key] = obj
