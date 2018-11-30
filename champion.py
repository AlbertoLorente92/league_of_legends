from stats import Stats


class Champion:
    key = 0
    name = ""
    stats = Stats()

    def __init__(self, champ_key):
        self.key = champ_key

    def __str__(self):
        return "Champion name: " + self.name + "\nChampion key: " + str(self.key)
