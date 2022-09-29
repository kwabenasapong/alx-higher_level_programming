#!/usr/bin/python3
'''List addition script'''
from sys import argv
'''
Write a script that adds all arguments to a Python list,
and then save them to a file:

    You must use your function save_to_json_file
    from 5-save_to_json_file.py

    You must use your function load_from_json_file
    from 6-load_from_json_file.py

    The list must be saved as a JSON representation
    in a file named add_item.json

    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
'''

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    def create_file():
        '''creates a json file and returns py_list'''
        py_list = []
        save_to_json_file(py_list, "add_item.json")
        py_list = load_from_json_file("add_item.json")
        return py_list

    try:
        py_list = load_from_json_file("add_item.json")
    except (FileNotFoundError):
        py_list = create_file()
    print('Cycle check-> {}'.format(py_list))
    py_list = load_from_json_file("add_item.json")
    for i in range(len(argv)):
        if i != 0:
            print('Check 1-> {}'.format(py_list))
            py_list.append(argv[i])
            print('Check 2-> {}'.format(py_list))
    save_to_json_file(py_list, "add_item.json")
    py_list = load_from_json_file("add_item.json")
    print('final check-> {}'.format(py_list))
