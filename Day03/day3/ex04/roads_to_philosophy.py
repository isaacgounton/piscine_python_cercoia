# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 4

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-26"

import sys
from bs4 import BeautifulSoup
import requests as req


def getSearchLink(search_result):
    soup = BeautifulSoup(search_result, "html.parser")

    p = soup.find(id="mw-content-text").p
    if p is not None:

        for i in p.find_all("a"):
            i = i.get("href")
            if i is not None \
                    and i[:6] == "/wiki/" \
                    and i[:11] != "/wiki/Help:" \
                    and i[:16] != "/wiki/Wikipedia:":
                return (soup.title.contents[0][:-12], i[6:])

    print("It leads to a dead end !", file=sys.stderr)
    return None


def doRequest(query):
    url = "https://en.wikipedia.org/w/index.php?search="
    r = req.get(url + query)
    if not r or r.status_code != 200:
        print("Request failed", file=sys.stderr)
        return None

    return getSearchLink(r.text)


def z(query):
    roads = [query]
    while True:
        road = doRequest(query)
        if road is None:
            return
        # print("road:", road)    # DEBUG
        roads.append(road[0])
        query = road[1]
        if query in roads:
            print("It leads to an infinite loop !", file=sys.stderr)
            return
        if query == "Philosophy":
            break

    print(
        "\n".join(roads) + "\nPhilosophy\n"
        + str(len(roads) + 2), "roads from", roads[0], "to philosophy !"
    )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        z(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "query", file=sys.stderr)
