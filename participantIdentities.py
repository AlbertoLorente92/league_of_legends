from player import Player


class ParticipantIdentities:
    participantId = 0
    player = Player()

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "participantId" in dict_info.keys():
                self.participantId = dict_info["participantId"]
            if "player" in dict_info.keys():
                self.player = Player(dict_info["player"])

    def __str__(self):
        return "ParticipantId: " + str(self.participantId)
