#!/usr/bin/python3
""" Console 0.0.1 Module"""
import cmd
from models.base_model import BaseModel
from models import FileStorage
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    """Defines console class"""

    prompt = '(hbnb) '

    __classes = {"BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
