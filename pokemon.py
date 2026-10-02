# How to import API in the python file
import requests
import json

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)

    if response.status_code == 200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retriev data{response.status_code}")
pokemon_name=input("Enter the pokemon name:")
pokemon_information=get_pokemon_info(pokemon_name)

if pokemon_information:
    print(f"Name= {pokemon_information['name']}")
    print(f"Id= {pokemon_information['id']}")
    print(f"Height= {pokemon_information['height']}")
    print(f"Weight= {pokemon_information['weight']}")