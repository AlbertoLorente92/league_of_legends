from creepsPerMinDeltas import CreepsPerMinDeltas
from damageTakenPerMinDeltas import DamageTakenPerMinDeltas
from goldPerMinDeltas import GoldPerMinDeltas
from xpPerMinDeltas import XpPerMinDeltas


class TimeLine:
    lane = ""
    participantId = 0
    role = ""
    creepsPerMinDeltas = CreepsPerMinDeltas()
    damageTakenPerMinDeltas = DamageTakenPerMinDeltas()
    goldPerMinDeltas = GoldPerMinDeltas()
    xpPerMinDeltas = XpPerMinDeltas()

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "lane" in dict_info.keys():
                self.lane = dict_info["lane"]
            if "participantId" in dict_info.keys():
                self.participantId = dict_info["participantId"]
            if "role" in dict_info.keys():
                self.role = dict_info["role"]
            if "creepsPerMinDeltas" in dict_info.keys():
                self.creepsPerMinDeltas = CreepsPerMinDeltas(dict_info["creepsPerMinDeltas"])
            if "damageTakenPerMinDeltas" in dict_info.keys():
                self.damageTakenPerMinDeltas = DamageTakenPerMinDeltas(dict_info["damageTakenPerMinDeltas"])
            if "goldPerMinDeltas" in dict_info.keys():
                self.goldPerMinDeltas = GoldPerMinDeltas(dict_info["goldPerMinDeltas"])
            if "xpPerMinDeltas" in dict_info.keys():
                self.xpPerMinDeltas = XpPerMinDeltas(dict_info["xpPerMinDeltas"])

    def __str__(self):
        return "ParticipantId: " + str(self.participantId) + "\n" + \
               "Lane: " + self.lane + "\n" + \
               "Role: " + self.role
