#!/usr/bin/python3
"""This is the console for the json file storage"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = [
        "BaseModel"
    ]

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
        class_name = line.split()[0]
        if len(line) == 0:
            print("** class name missing **")
        elif class_name not in self.__classes:
            print("** class doesn't exist **")
        else:
            pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
