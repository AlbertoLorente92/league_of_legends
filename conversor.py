from datetime import datetime, timedelta


def duration_game_str(duration):
    sec = timedelta(seconds=duration)
    d = datetime(1, 1, 1) + sec
    return str(d.minute) + ":" + str(d.second)


def queue_str(queue_id):
    if queue_id == 420:
        return "5v5 Ranked Solo games"
    elif queue_id == 440:
        return "5v5 Ranked Flex games"
    else:
        return "ERROR"


def season_str(season_id):
    if season_id == 11:
        return "SEASON 2018"
    elif season_id == 10:
        return "PRESEASON 2018"
    else:
        return "ERROR"


def team_str(team_id):
    if team_id == 100:
        return "Blue"
    elif team_id == 200:
        return "Red"
    else:
        return "ERROR"
