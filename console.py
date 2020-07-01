#!/usr/bin/python3
'''Cmd module'''
import cmd
import sys


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
        return True

    def do_empty_line(self):
        """
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
