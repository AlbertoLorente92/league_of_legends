import json


class Configuration:
    apikey = ""
    server = ""
    summonerName = ""

    def __init__(self, filename):
        with open(filename) as f:
            config = json.load(f)
        self.server = config["server"]
        self.apikey = config["apikey"]
        self.summonerName = config["summonerName"]
