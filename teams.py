from conversor import team_str


class Teams:
    firstBaron = 0
    firstBlood = 0
    firstDragon = 0
    firstInhibitor = 0
    teamId = 0
    win = ""

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "firstBaron" in dict_info.keys():
                self.firstBaron = dict_info["firstBaron"]
            if "firstBlood" in dict_info.keys():
                self.firstBlood = dict_info["firstBlood"]
            if "firstDragon" in dict_info.keys():
                self.firstDragon = dict_info["firstDragon"]
            if "firstInhibitor" in dict_info.keys():
                self.firstInhibitor = dict_info["firstInhibitor"]
            if "teamId" in dict_info.keys():
                self.teamId = dict_info["teamId"]
            if "win" in dict_info.keys():
                self.win = dict_info["win"]

    def __str__(self):
        return "Team: " + team_str(self.teamId) + "\n" + \
               "firstBaron: " + str(self.firstBaron) + "\n" + \
               "firstBlood: " + str(self.firstBlood) + "\n" + \
               "firstDragon: " + str(self.firstDragon) + "\n" + \
               "firstInhibitor: " + str(self.firstInhibitor) + "\n" + \
               "win: " + str(self.win)