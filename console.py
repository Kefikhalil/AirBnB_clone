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
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args.split()[0], args.split()[1])])
    def do_destroy(self, args):
        """Destroy command By ID
        """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """all
        """
        args = args.split()
        lst = []
        if args and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif not args:
            for i in storage.all().values():
                lst.append(str(i))
        else:
            for i in storage.all().values():
                if args[0] == i.__class__.__name__:
                    lst.append(str(i))
        if len(lst):
            print(lst)

    def do_update(self, args):
        """Update
        """
        _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            setattr(_all[key], args.split()[2],
                    re.search(r'\w+', args.split()[3]).group())
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
