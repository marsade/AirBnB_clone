#!/usr/bin/python3
"""This is the console for the json file storage"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = [
        "BaseModel"
    ]

    def parse(self, line):
        return line.split()

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        """Quits from the console"""
        return True

    def emptyline(self):
        """Does nothing when an empty line is passed"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class,
        saves it (to the JSON file) and prints the id.
        Ex: create <class>
        """
        words = self.parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif words[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(words[0])().id)
            storage.save()

    def do_show(self, line):
        words = self.parse(line)
        objdict = storage.all()
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) < 2:
            print("** instance id missing **")
        elif words[0] not in self.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(words[0], words[1]) not in objdict:
            print("** no instance found **")
        else:
            print(eval(words[0])())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
