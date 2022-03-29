#!/usr/bin/python3
""" This is the entry point of the command interpreter"""
import cmd , sys
from shlex import split
#from models import base_model
#from models.base_model import BaseModel
from turtle import *
import models
import re
 
CLASSES = {}


def parser(line):
    get_c_bracket = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)
    
    if get_c_bracket is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)] 
        else:
            lexer = split(line[:brackets.span()[0]]) # get the first index of the Regex
            return_line = [i.strip(",") for i in lexer]
            return_line.append(brackets.group())
            return return_line
    else:
        lexer = split(line[:get_c_bracket.span()[0]])
        return_line = [i.strip(",") for i in lexer]
        return_line.append(get_c_bracket.group())
        return return_line

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)-:: "

    __classes = {"BaseModel"} #,"User","State","City","Amenity","Place","Review"}

    def __init__(self, completekey: str = "tab", stdin = None, stdout = None) :
        super().__init__(completekey, stdin, stdout)


    def do_EOF(self, line):
        """quit CLI"""
        return True

    def do_quit(self, line):
        """Quit the command to exit the programm"""
        return True

    def do_create(self,line):
        """create new instance of BaseModel
            feat: save it (to JSON file) and prints the id
           """
        if len(line)  == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        else:
            baseModel = models.base_model.BaseModel

        try:
            save = models.classes[line]()
            models.base_model.storage.new(save) 
            models.base_model.storage.save()
            print(save.id)
        except Exception as e:
            print(e)


    
    def do_destroy(self):
        """deletes an instance based on the class name and id (save the change into the JSON file)"""
        pass

    def do_show(self):
        """display string representation of an instance based on the class name and id"""
        print()

        
    def do_all(self):
        """print all string representation of all instances based or not on the class name """
        pass

    def do_update(self):
        """update an instance based on the class name and id by adding or updating attribute (save the change into the json file)"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()