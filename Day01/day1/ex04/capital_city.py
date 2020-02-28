#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 4

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"

import sys


def find_city(argv):
    """Prend en argument un état (ex : Oregon) et affiche sur la sortie 
    standand sa capitale (ex : Salem) ou Unknow state"""

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

    if len(sys.argv) != 2:
        sys.exit(1)

    state = sys.argv[1]

    if state in states:
        response = capital_cities[states[state]]
    else:
        response = "Unknow state"

    print(response)


if __name__ == "__main__":
    find_city(sys.argv)
