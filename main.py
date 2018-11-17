import pprint
from api import json_info
from load_champs import list_of_champs
from load_configuration import load_configuration
from game import Game


def add_games(list_of_games, list_of_games_json):
    for game in list_of_games_json:
        g = Game(game["gameId"])
        g.champion = game["champion"]
        g.lane = game["lane"]
        g.platformId = game["platformId"]
        g.queue = game["queue"]
        g.role = game["role"]
        g.season = game["season"]
        g.timestamp = game["timestamp"]
        list_of_games.append(g)


def print_list_of_champs(champions_list):
    for champ in champions_list:
        print(champ)


def print_list_of_fames(list_of_games_f, champions_f):
    for i, g in enumerate(list_of_games_f):
        print("GAME ", i)
        g.print_game_info(champions_f)
        print("==========================================")


config = load_configuration("configuration.json")
champions = list_of_champs("champion.json")
list_of_games = []

# print_list_of_champs(champions)

# Program starts here
method_param = {"summonerName": config.summonerName}
json, exit_return, exit_error = json_info(config.apikey, config.server, "Info_Account", {}, method_param)
if exit_return != 0:
    print("Error number", exit_return, ":", exit_error)
else:
    method_param["accountId"] = json["accountId"]

# I want all data from all my rank games in soloQ from season 11
print(method_param["accountId"])
began = 0
end = 100
stop = False

while not stop:
    params = {"queue": 420, "beginIndex": began, "endIndex": end, "season": 11}  # Only rank games
    json, exit_return, exit_error = json_info(config.apikey, config.server, "MatchList_Account", params, method_param)
    if exit_return != 0:
        print("Error number", exit_return, ":", exit_error)
        stop = True
    else:
        #pprint.pprint(json["matches"])
        add_games(list_of_games, json["matches"])
        began += 100
        end += 100
        if len(json["matches"]) < 100:
            stop = True

print_list_of_fames(list_of_games, champions)



