import sys
from jsons_io import save_this_json, load_this_json
from api import json_info
from configuration import Configuration
from game import Game
from complete_game import CompleteGame
from cham_list import DictOfChampsAndStats


def add_games(list_of_games_f, list_of_games_json):
    for game in list_of_games_json:
        list_of_games_f.append(Game(game))


def print_list_of_games(list_of_games_f, champions_f):
    for i, g in enumerate(list_of_games_f):
        print("GAME ", i)
        g.print_game_info(champions_f)
        print("==========================================")


def show_me_everything(list_of_complete_games, champions):
    print("=============================")
    print("GAME INFO")
    print(list_of_complete_games[0])
    print("=============================")
    print("GAME INFO - Participant Identities")
    print(list_of_complete_games[0].participantIdentities[0])
    print("=============================")
    print("GAME INFO - Participant Identities - PLAYER")
    print(list_of_complete_games[0].participantIdentities[0].player)
    print("=============================")
    print("GAME INFO - Participants Info")
    list_of_complete_games[0].participants[0].print_participants_info(champions)
    print("=============================")
    print("GAME INFO - Participants Info - STATS")
    print(list_of_complete_games[0].participants[0].stats)
    print("=============================")
    print("GAME INFO - Participants Info - Timeline")
    print(list_of_complete_games[0].participants[0].timeline)
    print("=============================")
    print("GAME INFO - Participants Info - Timeline - creepsPerMinDeltas")
    print(list_of_complete_games[0].participants[0].timeline.creepsPerMinDeltas)
    print("=============================")
    print("GAME INFO - Participants Info - Timeline - damageTakenPerMinDeltas")
    print(list_of_complete_games[0].participants[0].timeline.damageTakenPerMinDeltas)
    print("=============================")
    print("GAME INFO - Participants Info - Timeline - goldPerMinDeltas")
    print(list_of_complete_games[0].participants[0].timeline.goldPerMinDeltas)
    print("=============================")
    print("GAME INFO - Participants Info - Timeline - xpPerMinDeltas")
    print(list_of_complete_games[0].participants[0].timeline.xpPerMinDeltas)
    print("=============================")
    print("GAME INFO - Teams")
    print(list_of_complete_games[0].teams[0])


def add_complete_games(list_of_complete_games_f, json_f):
    list_of_complete_games_f.append(CompleteGame(json_f))


def main(load_from_files, filename_account, filename_match_list, filename_match_info):
    print("PROGRAM STARTS.")
    if not load_from_files:
        print("Loading configuration...")
        config = Configuration("configuration.json")
        print("tConfiguration loaded.")
        method_param = {"summonerName": config.summonerName}

    print()
    print("Loading champions and stats...")
    champions = DictOfChampsAndStats("champion.json")
    print("Champions and stats loaded.")
    print()
    list_of_games = []
    list_of_complete_games = []
    print("Loading account info...")

    if load_from_files:
        json_response = load_this_json(filename_account + ".json")
    else:
        json_response = json_info(config, "Info_Account", {}, method_param)

    if json_response == "":
        sys.exit("===Error loading account info. Program stops.===")
    print("Account info loaded.")
    print()
    if "accountId" not in json_response.keys():
        sys.exit("===Error. 'accountId' isn't specified.===")

    if not load_from_files:
        save_this_json(filename_account + ".json", json_response)
        method_param["accountId"] = json_response["accountId"]
        params = {"queue": 420, "season": 11}

    print("AccountId:", json_response["accountId"])
    print()

    print("Loading match history...")
    # I want all data from all my rank games in soloQ (queue=420) from season 11 (season=11)
    began = 0
    end = 100
    stop = False
    while not stop:
        if load_from_files:
            json_response = load_this_json(filename_match_list + "_" + str(began) + "_" + str(end) + ".json")
        else:
            params["beginIndex"] = began  # Ask for blocks of 100 games
            params["endIndex"] = end
            json_response = json_info(config, "MatchList_Account", params, method_param)
        if json_response == "":
            stop = True
        else:
            add_games(list_of_games, json_response["matches"])
            began += 100
            end += 100
            if len(json_response["matches"]) < 100:  # If the block doesn't have 100 games it's the last block
                stop = True
    print("Match history loaded.")
    print()
    # print_list_of_games(list_of_games, champions)
    print("Loading every game....")
    x = 0
    while x in range(0, len(list_of_games)):
        if load_from_files:
            json_response = load_this_json(filename_match_info + "_" + str(list_of_games[x].gameId) + ".json")
        else:
            method_param["matchId"] = list_of_games[x].gameId
            json_response = json_info(config, "Info_Match", {}, method_param)
        if json_response == "" and not load_from_files:
            # Errors here aren't suppose to happen
            sys.exit("===Error. The file '" + filename_match_info + "_" + str(json_response["gameId"]) + ".json' doesn't exits.===")
        elif json_response == "" and load_from_files:
            sys.exit("===Error. Riot API shows an error.===")
        else:
            # pprint.pprint(json)
            if "gameId" in json_response.keys():
                print(x + 1, "/", len(list_of_games), "-", json_response["gameId"])
                if not load_from_files:
                    save_this_json(filename_match_info + "_" + str(json_response["gameId"]) + ".json", json_response)
                add_complete_games(list_of_complete_games, json_response)
                x += 1
    print("Every game loaded.")
    print()
    show_me_everything(list_of_complete_games, champions)


# Program starts here
fileName_account_static = "download_json/account"
fileName_match_list_static = "download_json/matchlist/matches"
fileName_match_info_static = "download_json/matches/match_info"
load_from_files_static = False
main(load_from_files_static, fileName_account_static, fileName_match_list_static, fileName_match_info_static)
