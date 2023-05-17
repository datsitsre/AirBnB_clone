#!/usr/bin/python3
"""
The console Model
"""
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """ Prompt to access """
    prompt = "(hbnb) "
    dict_models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_nothing(self, arg):
        """ No input """
        pass

    def do_quit(self, arg):
        """Close programm """
        return True

    def do_EOF(self, arg):
        """
            Ctrl-D close program
        """
        print("")
        return True

    def emptyline(self):
        """ emptyline  """
        pass

    def do_create(self, arg):
        """
            Create new models
        """
        if not arg:
            print("** class name missing **")
            return
        dict_data = shlex.split(arg)
        if dict_data[0] not in HBNBCommand.dict_models.keys():
            print("** class doesn't exist **")
            return
        dict_instance = HBNBCommand.dict_models[dict_data[0]]()
        dict_instance.save()
        print(dict_instance.id)

    def do_show(self, arg):
        """
            Print the created and updated_id
        """
        dict_keys = shlex.split(arg)
        if len(dict_keys) == 0:
            print("** class name missing **")
            return
        if dict_keys[0] not in HBNBCommand.dict_models.keys():
            print("** class doesn't exist **")
            return
        if len(dict_keys) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        dict_object = storage.all()
        key = dict_keys[0] + "." + dict_keys[1]
        if key in dict_object:
            obj_instance = str(dict_object[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
            Destroy objects
        """
        dict_keys = shlex.split(arg)
        if len(dict_keys) == 0:
            print("** class name missing **")
            return
        if dict_keys[0] not in HBNBCommand.dict_models.keys():
            print("** class doesn't exist **")
            return
        if len(dict_keys) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        dict_object = storage.all()
        key = dict_keys[0] + "." + dict_keys[1]
        if key in dict_object:
            del dict_object[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
            Model reresentation
        """
        storage.reload()
        json_dict = []
        objects_dict = storage.all()
        if not arg:
            for key in objects_dict:
                json_dict.append(str(objects_dict[key]))
            print(json.dumps(json_dict))
            return
        dict_key = shlex.split(arg)
        if dict_key[0] in HBNBCommand.dict_models.keys():
            for key in objects_dict:
                if dict_key[0] in key:
                    json_dict.append(str(objects_dict[key]))
            print(json.dumps(json_dict))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Make changes
        """
        if not arg:
            print("** class name missing **")
            return
        dict_data = shlex.split(arg)
        storage.reload()
        dict_object = storage.all()
        if dict_data[0] not in HBNBCommand.dict_models.keys():
            print("** class doesn't exist **")
            return
        if (len(dict_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = dict_data[0] + "." + dict_data[1]
            dict_object[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(dict_data) == 2):
            print("** attribute name missing **")
            return
        if (len(dict_data) == 3):
            print("** value missing **")
            return
        my_instance = dict_object[key]
        if hasattr(my_instance, dict_data[2]):
            data_type = type(getattr(my_instance, dict_data[2]))
            setattr(my_instance, dict_data[2], data_type(dict_data[3]))
        else:
            setattr(my_instance, dict_data[2], dict_data[3])
        storage.save()

    def do_update2(self, arg):
        """
        Structure: update [class name] [id] [dictionary]
        """
        if not arg:
            print("** class name missing **")
            return
        dict_modelsionary = "{" + arg.split("{")[1]
        dict_data = shlex.split(arg)
        storage.reload()
        dict_object = storage.all()
        if dict_data[0] not in HBNBCommand.dict_models.keys():
            print("** class doesn't exist **")
            return
        if (len(dict_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = dict_data[0] + "." + dict_data[1]
            dict_object[key]
        except KeyError:
            print("** no instance found **")
            return
        if (dict_modelsionary == "{"):
            print("** attribute name missing **")
            return

        dict_modelsionary = dict_modelsionary.replace("\'", "\"")
        dict_modelsionary = json.loads(dict_modelsionary)
        my_instance = dict_object[key]
        for my_key in dict_modelsionary:
            if hasattr(my_instance, my_key):
                data_type = type(getattr(my_instance, my_key))
                setattr(my_instance, my_key, dict_modelsionary[my_key])
            else:
                setattr(my_instance, my_key, dict_modelsionary[my_key])
        storage.save()

    def do_count(self, arg):
        """
        instances of a class
        """
        counter = 0
        objects_dict = storage.all()
        for key in objects_dict:
            if (arg in key):
                counter += 1
        print(counter)

    def default(self, arg):
        """ handle new ways of inputing data """
        val_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""
        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in val_dict.keys()):
            val_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
