import json
from stats import Stats


class DictOfChampsAndStats:
    dict_of_champs = {}
    dict_of_stats = {}

    def __init__(self, filename):
        with open(filename) as f:
            champions = json.load(f)
        for name, info in champions["data"].items():
            self.dict_of_champs[info["key"]] = info["name"]
            self.dict_of_stats[info["key"]] = Stats(info["stats"])

    def __str__(self):
        return "For printing all champs use 'printallchamps' function"

    def printallchamps(self):
        cad = ""
        for champ_key in self.dict_of_champs.keys():
            cad += self.getchampforid(champ_key) + " (" + champ_key + ")" + "\n"
        cad += cad[0:len(cad)-1]
        print(cad)

    def printallchampswithstats(self):
        cad = "=============================\n"
        for champ_key in self.dict_of_champs.keys():
            cad += self.getchampforid(champ_key) + " (" + champ_key + ")" + "\n"
            cad += self.getstatsforchampid(champ_key).__str__() + "\n"
            cad += "=============================\n"
        cad += cad[0:len(cad) - 1]
        print(cad)

    def getchampforid(self, champ_id):
        if str(champ_id) in self.dict_of_champs:
            return self.dict_of_champs[str(champ_id)]
        else:
            return "UNKNOWN CHAMP ID: " + str(champ_id)

    def getstatsforchampid(self, champ_id):
        if champ_id in self.dict_of_stats:
            return self.dict_of_stats[champ_id]
        else:
            return "UNKNOWN CHAMP ID: " + str(champ_id)
