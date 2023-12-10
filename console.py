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
        """Prints the string representation of an instance
        Ex: show <class> <class id>"""
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
            print(objdict["{}.{}".format(words[0], words[1])])

    def do_destroy(self, line):
        """Deletes an instance """
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
            del objdict["{}.{}".format(words[0], words[1])]
            storage.save()

    def do_all(self, line):
        """prints all string representations of all instances
        based or not on the class name
        Ex: all <class name> or all"""
        words = self.parse(line)
        objdict = storage.all()
        objlist = []
        if len(words) == 0:
            for obj_id in objdict.keys():
                obj = objdict[obj_id]
                obj_str = str(obj)
                objlist.append(obj_str)
            print(objlist)
        elif words[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for obj_id in objdict.keys():
                if words[0] in obj_id:
                    obj = objdict[obj_id]
                    obj_str = str(obj)
                    objlist.append(obj_str)
            print(objlist)

    def do_update(self, line):
        """Update an instance based on the class name by adding or 
        updating attribute"""
        words = self.parse(line)
        if len(words) > 5:
            words = words[0:5]
        print(words)   


if __name__ == '__main__':
    HBNBCommand().cmdloop()
