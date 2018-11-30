class Stats:
    armor = 0
    armorperlevel = 0
    attackdamage = 0
    attackdamageperlevel = 0
    attackrange = 0
    attackspeedoffset = 0
    attackspeedperlevel = 0
    crit = 0
    critperlevel = 0
    hp = 0
    hpperlevel = 0
    hpregen = 0
    hpregenperlevel = 0
    movespeed = 0
    mp = 0
    mpperlevel = 0
    mpregen = 0
    mpregenperlevel = 0
    spellblock = 0
    spellblockperlevel = 0
    key_champ = 0

    def __init__(self, dict_info={}):
        if dict_info != {}:
            if "armor" in dict_info.keys():
                self.armor = dict_info["armor"]
            if "armorperlevel" in dict_info.keys():
                self.armorperlevel = dict_info["armorperlevel"]
            if "attackdamage" in dict_info.keys():
                self.attackdamage = dict_info["attackdamage"]
            if "attackdamageperlevel" in dict_info.keys():
                self.attackdamageperlevel = dict_info["attackdamageperlevel"]
            if "attackrange" in dict_info.keys():
                self.attackrange = dict_info["attackrange"]
            if "attackspeedoffset" in dict_info.keys():
                self.attackspeedoffset = dict_info["attackspeedoffset"]
            if "attackspeedperlevel" in dict_info.keys():
                self.attackspeedperlevel = dict_info["attackspeedperlevel"]
            if "crit" in dict_info.keys():
                self.crit = dict_info["crit"]
            if "critperlevel" in dict_info.keys():
                self.critperlevel = dict_info["critperlevel"]
            if "hp" in dict_info.keys():
                self.hp = dict_info["hp"]
            if "hpperlevel" in dict_info.keys():
                self.hpperlevel = dict_info["hpperlevel"]
            if "hpregen" in dict_info.keys():
                self.hpregen = dict_info["hpregen"]
            if "hpregenperlevel" in dict_info.keys():
                self.hpregenperlevel = dict_info["hpregenperlevel"]
            if "movespeed" in dict_info.keys():
                self.movespeed = dict_info["movespeed"]
            if "mp" in dict_info.keys():
                self.mp = dict_info["mp"]
            if "mpperlevel" in dict_info.keys():
                self.mpperlevel = dict_info["mpperlevel"]
            if "mpregen" in dict_info.keys():
                self.mpregen = dict_info["mpregen"]
            if "mpregenperlevel" in dict_info.keys():
                self.mpregenperlevel = dict_info["mpregenperlevel"]
            if "spellblock" in dict_info.keys():
                self.spellblock = dict_info["spellblock"]
            if "spellblockperlevel" in dict_info.keys():
                self.spellblockperlevel = dict_info["spellblockperlevel"]

    def __str__(self):
        return "HP: " + str(self.hp) + "\n" + \
               "AD: " + str(self.attackdamage) + "\n" +  \
               "Crit: " + str(self.crit) + "\n" +  \
               "MovSpeed: " + str(self.movespeed) + "\n" +  \
               "ArmorDef: " + str(self.armor) + "\n" +  \
               "MagicDef: " + str(self.spellblock)
