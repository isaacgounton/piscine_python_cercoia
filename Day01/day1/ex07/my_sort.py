# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 7

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"


def tri():
    """Classement du dictionnaire"""

    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    musicians = {name: year for name, year in sorted(
        d.items(), key=lambda item: item[1])}

    for name, year in musicians.items():
        print(name)


if __name__ == "__main__":
    tri()
