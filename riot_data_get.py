import threading
import time
from Player import Player

api_key = 'RGAPI-4c6c64c1-1365-461f-a004-732c7891cc36'
root = "https://na1.api.riotgames.com/"
account_end_point = "lol/summoner/v4/summoners/by-name/"
live_game_end_point = "lol/spectator/v4/active-games/by-summoner/"
import requests
import json


def get_accunt_info(my_name):
    response = requests.get(root + account_end_point + my_name + "?api_key=" + api_key)
    account_me = json.loads(response.text)
    return account_me


def has_cur_game(player_id):
    response = requests.get(root + live_game_end_point + player_id + "?api_key=" + api_key)
    now_game = json.loads(response.text)
    type(now_game)
    if now_game.get('gameId') != None:
        return True
    else:
        return False


def get_game_time(player_id):
    response = requests.get(root + live_game_end_point + player_id + "?api_key=" + api_key)
    now_game = json.loads(response.text)
    game_len = now_game["gameLength"]
    game_len += 160
    return game_len


def get_game_response(player_id):
    response = requests.get(root + live_game_end_point + player_id + "?api_key=" + api_key)
    now_game = json.loads(response.text)
    return now_game


class Game:

    def __init__(self, name):
        self.name = name
        user_id = get_accunt_info(name)["id"]
        self.user_id = user_id
        self.in_game = False
        self.game_mode = None
        self.cham_list = None
        self.start_time = None
        update_thread = threading.Thread(target=self.update)
        update_thread.start()

    def get_start_time(self, game_info):
        game_len = game_info["gameLength"] + 160
        ts = time.time()
        ts -= game_len
        self.start_time = ts

    def update(self):

        while True:
            game_info = get_game_response(self.user_id)
            if game_info.get('gameId') is not None:
                self.in_game = True
            else:
                self.in_game = False

            if self.in_game:
                op_team = self.get_op_team(game_info)
                self.cham_list = [x.cham for x in op_team]
                self.game_mode = game_info["gameMode"]
                self.get_start_time(game_info)

                print("in game")
            else:
                print("not in game, try in 10s")
            time.sleep(10)

    def get_op_team(self, game_info):
        players = game_info["participants"]
        my_team = []
        op_team = []
        op_is_1 = True
        for player_info in players:
            player = Player(player_info)
            if player.name == self.name and player.team == 100:
                op_is_1 = False
            if player.team == 100:
                my_team.append(player)
            else:
                op_team.append(player)

        if op_is_1:
            my_team, op_team = op_team, my_team
        return op_team

# response = requests.get(root + "liveclientdata/playermainrunes?summonerName=" + "?api_key=" + api_key)
# now_game = json.loads(response.text)
# print(now_game)
# game_len = now_game["gameLength"]


# # 60 + 100
# import time
#
# # ts stores the time in seconds
# g_len = get_game_time(get_accunt_info("dogxxy")["id"])
# print(g_len)
# ts = time.time()
#
# print(ts)
# ts-= g_len
# print(ts)
# from datetime import datetime
# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


# print(game_mode)
#
#
# players = now_game["participants"]
# my_team = []
# op_team = []
# op_is_1 = True
# for player_info in players:
#     player = Player(player_info)
#     if player.name == my_name and player.team == 100:
#         op_is_1 = False
#     if player.team == 100:
#         my_team.append(player)
#     else:
#         op_team.append(player)
#
# if op_is_1:
#     my_team,op_team = op_team,my_team
#
# for player in op_team:
#     print(player.cham,player.name)
#
# print()
# for player in my_team:
#     print(player.cham,player.name)
#
#
#
#
#
# # print(player)
#
# #
# # https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/hZXx9UhgIbfjq6_kxqbMN7-m7PTiTJj65oOPNSOHLqTEsig?api_key=RGAPI-4c6c64c1-1365-461f-a004-732c7891cc36
#
#
#
