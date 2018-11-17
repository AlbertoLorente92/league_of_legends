def show_list_of_games_info(CHAMPIONS, matches):
    for game, info_game in enumerate(matches):
        print("GAME " + str(game + 1) + ":")
        print_game_info(CHAMPIONS, info_game)
        print("===================================")


def show_list_of_games_info_ranked(CHAMPIONS, matches):
    for game, info_game in enumerate(matches):
        if info_game["queue"] == 420:
            print("GAME " + str(game + 1) + ":")
            print_game_info(CHAMPIONS, info_game)
            print("===================================")