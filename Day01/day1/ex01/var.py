#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 1

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-24"


def my_var():
    """Type des variables"""

    var_list = [43, "43", "quarante-trois",
                43.0, True, [43], {43: 43}, (43,), set()]
    for var in var_list:
        print(f"{var} est de type {type(var)}")


if __name__ == "__main__":
    my_var()
