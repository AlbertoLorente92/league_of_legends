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

    def __str__(self):
        return "HP: " + str(self.hp) + "\n" + \
               "AD: " + str(self.attackdamage) + "\n" +  \
               "Crit: " + str(self.crit) + "\n" +  \
               "MovSpeed: " + str(self.movespeed) + "\n" +  \
               "ArmorDef: " + str(self.armor) + "\n" +  \
               "MagicDef: " + str(self.spellblock)
