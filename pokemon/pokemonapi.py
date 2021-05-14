#!/usr/bin/env python3

# imports always go at the top of your code
import request

def main():
    

    pokename = input ("Enter the pokemon of your choice: ")
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokenamue}").json()

    print(pokeapi)

main()

