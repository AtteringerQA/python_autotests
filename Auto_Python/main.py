import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='46aaaa55ebd240a9992ea6e9e9541744'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
body_created_pokemon = {
    "name": "generate",
    "photo_id": 7
}

body_put = {
    "pokemon_id": "44446",
    "name": "Squirtle",
    "photo_id": 7
}

body_pokeball = {
    "pokemon_id": "44446"
}


'''response_created = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_created_pokemon)
print(response_created.text)'''

'''response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put )
print(response_put.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)