from participantIdentities import ParticipantIdentities
from teams import Teams
from participants import Participants
from conversor import duration_game_str, queue_str, season_str

class CompleteGame:
    gameCreation = 0
    gameDuration = 0
    gameId = 0
    gameMode = ""
    gameType = ""
    gameVersion = ""
    mapId = 0
    platformId = ""
    queueId = 0
    seasonId = 0
    participantIdentities = [ParticipantIdentities()]
    teams = [Teams()]
    participants = [Participants()]

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "gameCreation" in dict_info.keys():
                self.gameCreation = dict_info["gameCreation"]
            if "gameDuration" in dict_info.keys():
                self.gameDuration = dict_info["gameDuration"]
            if "gameId" in dict_info.keys():
                self.gameId = dict_info["gameId"]
            if "gameMode" in dict_info.keys():
                self.gameMode = dict_info["gameMode"]
            if "gameType" in dict_info.keys():
                self.gameType = dict_info["gameType"]
            if "gameVersion" in dict_info.keys():
                self.gameVersion = dict_info["gameVersion"]
            if "mapId" in dict_info.keys():
                self.mapId = dict_info["mapId"]
            if "platformId" in dict_info.keys():
                self.platformId = dict_info["platformId"]
            if "queueId" in dict_info.keys():
                self.queueId = dict_info["queueId"]
            if "seasonId" in dict_info.keys():
                self.seasonId = dict_info["seasonId"]
            if "participantIdentities" in dict_info.keys():
                self.participantIdentities = [ParticipantIdentities(p) for p in dict_info["participantIdentities"]]
            if "participants" in dict_info.keys():
                self.participants = [Participants(p) for p in dict_info["participants"]]
            if "teams" in dict_info.keys():
                self.teams = [Teams(p) for p in dict_info["teams"]]

    def __str__(self):
        return "GameId: " + str(self.gameId) + "\n" + \
               "GameDuration: " + duration_game_str(self.gameDuration) + "\n" + \
               "GameMode: " + str(self.gameMode) + "\n" + \
               "GameType: " + str(self.gameType) + "\n" + \
               "QueueId: " + queue_str(self.queueId) + "\n" + \
               "SeasonId: " + season_str(self.seasonId)
