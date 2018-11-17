import requests


def create_string_request(key, server, method, params):
    cad = "https://" + server + ".api.riotgames.com" + method
    cont = 0
    for key_param, value in params.items():
        if cont == 0:
            cad += "?" + key_param + "=" + str(value)
        else:
            cad += "&" + key_param + "=" + str(value)
        cont += 1
    if cont == 0:
        cad += "?api_key=" + key
    else:
        cad += "&api_key=" + key
    return cad


def execute_request(command):
    return requests.get(command)


def replace_params_method(method, method_params):
    for key, value in method_params.items():
        method = method.replace("{" + key + "}", str(value))
    return method


def json_info(key, server, method, params, method_params):
    if key == "":
        return "", 1, "Key not informed"
    if server == "":
        return "", 2, "Server not informed"

    method_aux = ""
    if method == "Info_Account":
        method_aux = "/lol/summoner/v3/summoners/by-name/{summonerName}"
    elif method == "MatchList_Account":
        method_aux = "/lol/match/v3/matchlists/by-account/{accountId}"
    elif method == "Info_Match":
        method_aux = "/lol/match/v3/matches/{matchId}"
    else:
        return "", 3, "Method not matched"

    method_aux = replace_params_method(method_aux, method_params)
    if "{" in method_aux or "}" in method_aux:
        return "", 4, "Insufficient parameters for the method"

    return execute_request(create_string_request(key, server, method_aux, params)).json(), 0, ""
