import json
from configuration import Configuration


def load_configuration(filename):
    with open(filename) as f:
        config = json.load(f)

    config_obj = Configuration()
    config_obj.server = config["server"]
    config_obj.apikey = config["apikey"]
    config_obj.summonerName = config["summonerName"]
    return config_obj
