import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='46aaaa55ebd240a9992ea6e9e9541744'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = '4347'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : TRAINER_ID})
    assert response.status_code == 200

def test_name_mytrener ():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json () ["data"] [0] ["trainer_name"] == 'Atteringer II'