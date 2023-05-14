import json


def load_operations(filename):
    with open(filename, 'r', encoding='utf') as file:
        data = json.load(file)
    return data

