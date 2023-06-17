#!/usr/bin/python3
import json
import csv


class Base:
    """Base class for other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        my_list = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        fname = cls.__name__ + '.json'
        with open(fname, 'w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of instances from the JSON string representation"""
        return json.loads(json_string or '[]')

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        my_list = []
        fname = cls.__name__ + '.json'
        if fname and os.path.isfile(fname):
            with open(fname, 'r') as f:
                listjson = cls.from_json_string(f.read())
                my_list = [cls.create(**l) for l in listjson]
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list objects in CSV format and saves"""
        fname = cls.__name__ + '.csv'
        fieldnames = cls.get_fieldnames()
        with open(fname, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs or []:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV of the list of instances"""
        my_list = []
        fname = cls.__name__ + '.csv'
        if fname and os.path.isfile(fname):
            with open(fname, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dictionary = {key: int(value) for key, value in row.items()}
                    my_list.append(cls.create(**dictionary))
        return my_list

    @classmethod
    def get_fieldnames(cls):
        """Returns the fieldnames for CSV serialization"""
        if cls.__name__ == 'Rectangle':
            return ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            return ['id', 'size', 'x', 'y']
