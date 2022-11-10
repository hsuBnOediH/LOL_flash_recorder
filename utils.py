import  requests
import  json

def get_version():

    response = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    version_list = json.loads(response.text)
    latest_version = version_list[0]
    return latest_version


def get_id_to_cham():
    version_str = get_version()

    response = requests.get("https://ddragon.leagueoflegends.com/cdn/"+version_str + "/data/en_US/champion.json")
    raw_data = json.loads(response.text)['data']

    id2cham = {}
    for cham_name in raw_data:
        cham_id = int(raw_data[cham_name]["key"])
        id2cham[cham_id] = cham_name
    return id2cham

def get_id_to_spell():
    version_str = get_version()
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/"+ version_str+"/data/en_US/summoner.json")
    raw_data = json.loads(response.text)['data']
    id2spell = {}
    for spell_name in raw_data:
        spell_id = int(raw_data[spell_name]["key"])
        id2spell[spell_id] = spell_name[8:]
    return id2spell




