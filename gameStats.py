class GameStats:
    assists = 0
    deaths = 0
    kills = 0
    magicDamageDealtToChampions = 0
    magicalDamageTaken = 0
    physicalDamageDealtToChampions = 0
    totalDamageDealtToChampions = 0
    physicalDamageTaken = 0
    totalDamageTaken = 0
    participantId = 0
    totalHeal = 0
    visionScore = 0
    visionWardsBoughtInGame = 0
    wardsKilled = 0
    wardsPlaced = 0
    win = ""

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "assists" in dict_info.keys():
                self.assists = dict_info["assists"]
            if "deaths" in dict_info.keys():
                self.deaths = dict_info["deaths"]
            if "kills" in dict_info.keys():
                self.kills = dict_info["kills"]
            if "magicDamageDealtToChampions" in dict_info.keys():
                self.magicDamageDealtToChampions = dict_info["magicDamageDealtToChampions"]
            if "magicalDamageTaken" in dict_info.keys():
                self.magicalDamageTaken = dict_info["magicalDamageTaken"]
            if "physicalDamageDealtToChampions" in dict_info.keys():
                self.physicalDamageDealtToChampions = dict_info["physicalDamageDealtToChampions"]
            if "totalDamageDealtToChampions" in dict_info.keys():
                self.totalDamageDealtToChampions = dict_info["totalDamageDealtToChampions"]
            if "magicDamageDealtToChampions" in dict_info.keys():
                self.magicDamageDealtToChampions = dict_info["magicDamageDealtToChampions"]
            if "physicalDamageTaken" in dict_info.keys():
                self.physicalDamageTaken = dict_info["physicalDamageTaken"]
            if "totalDamageTaken" in dict_info.keys():
                self.totalDamageTaken = dict_info["totalDamageTaken"]
            if "participantId" in dict_info.keys():
                self.participantId = dict_info["participantId"]
            if "totalHeal" in dict_info.keys():
                self.totalHeal = dict_info["totalHeal"]
            if "visionScore" in dict_info.keys():
                self.visionScore = dict_info["visionScore"]
            if "visionWardsBoughtInGame" in dict_info.keys():
                self.visionWardsBoughtInGame = dict_info["visionWardsBoughtInGame"]
            if "wardsKilled" in dict_info.keys():
                self.wardsKilled = dict_info["wardsKilled"]
            if "wardsPlaced" in dict_info.keys():
                self.wardsPlaced = dict_info["wardsPlaced"]
            if "totalHeal" in dict_info.keys():
                self.win = dict_info["win"]

    def __str__(self):
        return  "ParticipantId: " + str(self.participantId) + "\n" + \
                "Win: " + str(self.win) + "\n" + \
                "K/D/A: " + str(self.kills) + "/" + str(self.deaths) + "/" + str(self.assists) + "\n" + \
                "TotalDamageDealtToChampions: " + str(self.totalDamageDealtToChampions) + "\n" + \
                "TotalDamageTaken: " + str(self.totalDamageTaken)
