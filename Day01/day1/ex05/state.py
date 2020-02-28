import sys

# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 5

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"


def find_state(argv):

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    states_rev = {key: value for value, key in states.items()}
    capital_cities_rev = {key: value for value, key in capital_cities.items()}

    if len(sys.argv) != 2:
        sys.exit(1)

    city = sys.argv[1]

    if city in capital_cities_rev:
        response = states_rev[capital_cities_rev[city]]
    else:
        response = "Unknow state"

    print(response)


if __name__ == "__main__":
    find_state(sys.argv)
