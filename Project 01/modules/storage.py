import json
import os

FILE_PATH = "data/classes.json"


def load_classes():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_classes(class_list):
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(FILE_PATH, "w") as file:
        json.dump(class_list, file, indent=4)

