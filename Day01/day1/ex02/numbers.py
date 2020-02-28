#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 2

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"


def numbers():
    """Afficher les nombres dans un fichier"""

    with open("numbers.txt", "r") as f:
        numbers_var = f.read().split(",")

        for number in numbers_var:
            print(number)


if __name__ == "__main__":
    numbers()
