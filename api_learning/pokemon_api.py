import requests
import json

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_response_data = response.json()
        print("saved file")
        with open("api_response.txt", "w") as file:
            json.dump(pokemon_response_data, file, indent=4)
    else:
        print(f"Failed to retrive the Data {response.status_code}")

pokemon_name = 'pikachu'

get_pokemon_info(pokemon_name)