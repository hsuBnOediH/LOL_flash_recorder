from utils import get_id_to_cham,get_id_to_spell



class Player:

    id2cham = get_id_to_cham()
    id2spell = get_id_to_spell()
    def __init__(self,player_d):
        self.team = player_d['teamId']
        self.cham =self.id2cham[player_d['championId']]
        spell_l = [self.id2spell[player_d['spell1Id']],self.id2spell[player_d['spell2Id']]]
        self.has_false = "Flash" in spell_l
        self.name = player_d['summonerName']
        self.id = player_d['summonerId']