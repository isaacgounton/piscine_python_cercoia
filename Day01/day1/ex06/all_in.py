# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 6

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"

import sys


def arg_list(chaine):
    my_list = [item for item in chaine.split(",")]
    my_list = [item.strip().title()
               for item in my_list if item != "" and item != "\t"]
    return my_list


def find_any(argv):
    """Trouver une ville ou un etat; ou encore rien"""

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

    my_list = arg_list(sys.argv[1])

    for item in my_list:
        if item in states:
            print(
                f"{item} is the state of {capital_cities[states[item]]} (akr: {states[item]}")
        elif item in capital_cities_rev:
            print(
                f"{item} is the capital city of {states_rev[capital_cities_rev[item]]} (akr: {capital_cities_rev[item]})")
        else:
            print(f"{item} is neither a capital city nor a state.")


if __name__ == "__main__":
    find_any(sys.argv)
