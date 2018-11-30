class Game:
    gameId = 0
    lane = ""
    champion = 0
    platformId = ""
    timestamp = 0
    queue = 0
    role = ""
    season = 0

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "gameId" in dict_info.keys():
                self.gameId = dict_info["gameId"]
            if "lane" in dict_info.keys():
                self.lane = dict_info["lane"]
            if "champion" in dict_info.keys():
                self.champion = dict_info["champion"]
            if "platformId" in dict_info.keys():
                self.platformId = dict_info["platformId"]
            if "timestamp" in dict_info.keys():
                self.timestamp = dict_info["timestamp"]
            if "queue" in dict_info.keys():
                self.queue = dict_info["queue"]
            if "role" in dict_info.keys():
                self.role = dict_info["role"]
            if "season" in dict_info.keys():
                self.season = dict_info["season"]

    def __str__(self):
        return "Use function 'print_game_info'"

    def print_game_info(self, champions):
        print("GameID:", self.gameId)
        print("Champ:", champions[self.champion], "(", self.champion, ")")
        print("Lane:", self.lane)
        print("Queue:", self.queue)


