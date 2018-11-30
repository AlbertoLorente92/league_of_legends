from conversor import team_str
from gameStats import GameStats
from timeline import TimeLine


class Participants:
    championId = 0
    highestAchievedSeasonTier = ""
    participantId = 0
    spell1Id = 0
    spell2Id = 0
    stats = GameStats()
    teamId = 0
    timeline = TimeLine()

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "championId" in dict_info.keys():
                self.championId = dict_info["championId"]
            if "highestAchievedSeasonTier" in dict_info.keys():
                self.highestAchievedSeasonTier = dict_info["highestAchievedSeasonTier"]
            if "participantId" in dict_info.keys():
                self.participantId = dict_info["participantId"]
            if "spell1Id" in dict_info.keys():
                self.spell1Id = dict_info["spell1Id"]
            if "spell2Id" in dict_info.keys():
                self.spell2Id = dict_info["spell2Id"]
            if "teamId" in dict_info.keys():
                self.teamId = dict_info["teamId"]
            if "stats" in dict_info.keys():
                self.stats = GameStats(dict_info["stats"])
            if "timeline" in dict_info.keys():
                self.timeline = TimeLine(dict_info["timeline"])

    def __str__(self):
        return "Use 'print_participants_info' function"

    def print_participants_info(self, champions):
        print("ParticipantId:", self.participantId)
        print("Champion:", champions.getchampforid(self.championId), "(", self.championId, ")")
        print("Tier:", self.highestAchievedSeasonTier)
        print("Team:", team_str(self.teamId))
