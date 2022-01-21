#!/usr/bin/python3
""" This is the entry point of the command interpreter"""
import cmd , sys
from turtle import *

class ConComand(cmd.Cmd):
    
    intro = """\
        Documented commands (type help <topic>):\n
        ========================================\n
        EOF  help  quit"""

    prompt = "(hbnb)"

    def __init__(self, completekey: str = "tab", stdin = None, stdout = None) :
        super().__init__(completekey, stdin, stdout)
    
    def do_greet(self, line):
        """display interactive intro"""
        print(intro)

    def do_EOF(self, line):
        """quit CLI"""
        return True

    def do_quit(self, line):
        """Quit the command to exit the programm"""
        return True

    def do_create(self,line):
        """create new instance of BaseModel"""
    
    def do_destroy(self):
        """deletes an instance based on the class name and id (save the change into the JSON file)"""


    def do_show(self):
        """display string representation of an instance based on the class name and id"""

    def do_all(self):
        """print all string representation of all instances based or not on the class name """

    def do_update(self):
        """update an instance based on the class name and id by adding or updating attribute (save the change into the json file)"""


if __name__ == "__main__":
    ConComand().cmdloop()
