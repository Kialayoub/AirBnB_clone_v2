#!/usr/bin/python3
"""This module implements the FileStorage class for AirBnB"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON files to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Args:
            cls (class): The class type to filter.

        Returns:
            dict: A dictionary of objects.
        """
        if cls is None:
            return self.__objects
        filtered_objects = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                filtered_objects[key] = obj
        return filtered_objects

    def new(self, obj):
        """Sets the __objects dictionary with the given object.

        Args:
            obj: The object to be set.
        """
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    class_name = value["__class__"]
                    loaded_obj = eval(class_name)(**value)
                    self.__objects[key] = loaded_obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists.

        Args:
            obj: The object to be deleted.
        """
        if obj is not None:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            if k in self.__objects:
                del self.__objects[k]
                self.save()

    def close(self):
        """Deserializes the JSON file to objects."""
        self.reload()
