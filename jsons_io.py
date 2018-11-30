import json


def save_this_json(filename, json_obj):
    with open(filename, "w") as fp:
        json.dump(json_obj, fp)


def load_this_json(filename):
    with open(filename, "r") as fp:
        data = json.load(fp)
    return data
