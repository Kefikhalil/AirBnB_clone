#!/usr/bin/python3
'''Cmd module'''
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    '''the command interpreter'''
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        print('')
        return True

    def emptyline(self):
        """
        """
        pass

    def do_show(self, args):
        """Do show
        """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")
            

if __name__ == "__main__":
    HBNBCommand().cmdloop()
