class Game:
    id = 0
    lane = ""
    champion = 0
    platformId = ""
    timestamp = 0
    queue = 0
    role = ""
    season = 0

    def __init__(self, game_id):
        self.id = game_id

    def __str__(self):
        return ""

    def print_game_info(self, champions):
        print("GameID:", self.id)
        print("Champ:", self.champion_name(champions), "(", self.champion, ")")
        print("Lane:", self.lane)
        print("Queue:", self.queue)

    def champion_name(self, champions):
        for champ in champions:
            if int(champ.key) == int(self.champion):
                return champ.name
        return "Error"
