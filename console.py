#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    The entry point for the command interpreter
    """
    prompt = ("(hbnb)")
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass

    def do_create(self, line):
        """
        Usage: create <class name>

        Creates a new instance of BaseModel, saves it (JSON file) & prints id

        Ex: $ create BaseModel
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if line[0] == 'BaseModel':
                obj = BaseModel()
            elif line[0] == 'User':
                obj = User()
            elif line[0] == 'Place':
                obj = Place()
            elif line[0] == 'State':
                obj = State()
            elif line[0] == 'City':
                obj = City()
            elif line[0] == 'Amenity':
                obj = Amenity()
            elif line[0] == 'Review':
                obj = Review()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        Usage: show <class name> <id>

        Prints the string rep. of an instance based on the class name & id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            obj = objects.get(key, None)
            if key not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[key])
