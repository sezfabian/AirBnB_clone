#!/usr/bin/python3
"""Class BaseModel module"""

import uuid
import datetime
from models import storage


class BaseModel:
    """"Defines BaseModel object class"""

    def __init__(self, *args, **kwargs):
        """initializes class instance"""
        if kwargs is not None and kwargs != {}:
            self.__dict__.update(kwargs)
            self.__dict__["created_at"] = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.my_number = None
            self.name = None
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns an informal string representation of a BaseModel instance
        [<class name>] (<self.id>) <self.__dict__>
        """
        return str("[{}] ({}) {}".format(type(self).__name__,
                   self.id, self.__dict__))

    def save(self):
        """
        Updates public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of __dict__ of the instance
        """
        _dict = self.__dict__.copy()
        _dict["__class__"] = type(self).__name__
        _dict["created_at"] = _dict["created_at"].isoformat()
        _dict["updated_at"] = _dict["updated_at"].\
        strftime("%Y-%m-%dT%H:%M:%S.%f")
        return _dict