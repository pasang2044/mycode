#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests



def main():


    """runtime code"""

    response = requests.get('http://api.open-notify.org/astros.json').json()

    print(f"Number in space: {response['number']}")
    for x in response['people']:

        print(f"{x['name']} is on the {x['craft']}.")

if __name__ == "__main__":
    main()

