class Player:
    accountId = 0
    currentAccountId = 0
    currentPlatformId = ""
    matchHistoryUri = ""
    platformId = ""
    profileIcon = 0
    summonerId = 0
    summonerName = ""

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "accountId" in dict_info.keys():
                self.accountId = dict_info["accountId"]
            if "currentAccountId" in dict_info.keys():
                self.currentAccountId = dict_info["currentAccountId"]
            if "currentPlatformId" in dict_info.keys():
                self.currentPlatformId = dict_info["currentPlatformId"]
            if "matchHistoryUri" in dict_info.keys():
                self.matchHistoryUri = dict_info["matchHistoryUri"]
            if "platformId" in dict_info.keys():
                self.platformId = dict_info["platformId"]
            if "profileIcon" in dict_info.keys():
                self.profileIcon = dict_info["profileIcon"]
            if "summonerId" in dict_info.keys():
                self.summonerId = dict_info["summonerId"]
            if "summonerName" in dict_info.keys():
                self.summonerName = dict_info["summonerName"]

    def __str__(self):
        return "SummonerName: " + str(self.summonerName) + " (" + str(self.accountId) + ")"
