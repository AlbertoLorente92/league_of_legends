import json
from champion import Champion
from stats import Stats


def list_of_champs(filename):
    with open(filename) as f:
        champions = json.load(f)
    list_of_champs = []
    for name, info in champions["data"].items():
        champ = Champion(info["key"])
        champ.name = info["name"]
        champ.id = info["id"]
        champ_stats = Stats()
        champ_stats.armor = info["stats"]["armor"]
        champ_stats.armorperlevel = info["stats"]["armorperlevel"]
        champ_stats.attackdamage = info["stats"]["attackdamage"]
        champ_stats.attackdamageperlevel = info["stats"]["attackdamageperlevel"]
        champ_stats.attackrange = info["stats"]["attackrange"]
        champ_stats.attackspeedoffset = info["stats"]["attackspeedoffset"]
        champ_stats.attackspeedperlevel = info["stats"]["attackspeedperlevel"]
        champ_stats.crit = info["stats"]["crit"]
        champ_stats.critperlevel = info["stats"]["critperlevel"]
        champ_stats.hp = info["stats"]["hp"]
        champ_stats.hpperlevel = info["stats"]["hpperlevel"]
        champ_stats.hpregen = info["stats"]["hpregen"]
        champ_stats.hpregenperlevel = info["stats"]["hpregenperlevel"]
        champ_stats.movespeed = info["stats"]["movespeed"]
        champ_stats.mp = info["stats"]["mp"]
        champ_stats.mpperlevel = info["stats"]["mpperlevel"]
        champ_stats.mpregen = info["stats"]["mpregen"]
        champ_stats.mpregenperlevel = info["stats"]["mpregenperlevel"]
        champ_stats.spellblock = info["stats"]["spellblock"]
        champ_stats.spellblockperlevel = info["stats"]["spellblockperlevel"]
        champ.stats = champ_stats
        list_of_champs.append(champ)
    return list_of_champs
