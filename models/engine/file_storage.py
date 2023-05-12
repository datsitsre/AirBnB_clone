#!/usr/bin/python3

import json


class FileStorage:
    """
        Name : File Storage class
        Attributes :
        Method :
    """

    """
        Private class
    """
    __file_path = "file.json"
    __objects = {}



    def all(self):
        """
            returns the object
        """
        return self.__objects

    def new(self, obj):
        """
            Sets the __objects
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj


    def save(self):
        """
            Serializes __objects
        """
        diction_object_json = {}
        for data in self.__objects:
            diction_object_json[data] = self.__objects[data].to_dict()
        """ write the data to json file """
        with open(self.__file_path, 'w') as file_data:
            json.dump(diction_object_json, file_data) 
    
    def reload(self):
        """ Deserialize the json file __objects """
        try:
            with open(self.__file_path, 'r')  as file_data:
                json_data = json.load(file_data)
        except:
            pass
