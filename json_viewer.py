from genericpath import exists
import pprint
import json
import sys
from _collections_abc import Iterable


global_path = []
def read_json(path):
    if exists(path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("File doesn't contain json objects")
    else:
        print("There is no such path")


def view_json(data):
    global global_path
    if isinstance(data, Iterable):
        view = input("Do you want to see (1)available entries or (2)actual file(1/2)\n")
        if view == "1":
            show_available_entries(data)
        elif view == "2":
            pprint.pprint(data)
            show_available_entries(data)
        entry = input()
        if isinstance(data, dict):
            if entry in data.keys():
                global_path.append(entry)
                view_json(data[entry])
            else:
                print("There is no such entry in object")
        elif isinstance(data, list):
            if entry.isdecimal() and int(entry) < len(data) - 1:
                global_path.append(int(entry))
                view_json(data[int(entry)])
            else:
                print("There is no that much entries in object")
    else:
        print("this object contains only from 1 element")
        pprint.pprint(data)
    print("do you want to return on previous level?(Y/exit)")
    user_exit = input()
    if user_exit in "Yy":
        data = read_json("twitter1.json")
        for layer in global_path[:-1]:
            data = data[layer]
        view_json(data)
    else:
        sys.exit()


def show_available_entries(data):
    if isinstance(data, dict):
        available_keys = list(data.keys())
        print(*available_keys)
    else:
        print(f"The current object is list with {len(data)}")
        print("you can see any element of this list")
        print(data)


def open_key(data, key):
    return data[key]

def main(path):
    data = read_json(path)
    view_json(data)


if __name__ == "__main__":
    main("twitter2.json")

