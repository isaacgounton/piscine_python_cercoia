# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 1

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-26"

import sys
from antigravity import geohash


def geohash_it(latitude, longitude, datedow):
    """
    Calculate geohash from latitude longitude datedow
    then print it on stdout.

    https://xkcd.com/353/
    https://xkcd.com/426/
    """
    geohash(float(latitude), float(
        longitude), str(datedow).encode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        geohash_it(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print(
            "Usage:", sys.argv[0],
            "latitude longitude datedow\n"
            "Exemple:", sys.argv[0],
            "37.421542 -122.085589 2005-05-26-10458.68"
        )
        #geohash_it(37.421542, -122.085589, b'2005-05-26-10458.68')
