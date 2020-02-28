# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 2

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-26"

import local_lib.path as path


def program():
    """Mon programme"""

    try:
        path.os.makedirs('folder', exist_ok=True)
        with open('./folder/file.txt', 'a+') as fd:
            fd.write("CERCO IA\n")
        with open('./folder/file.txt', 'r+') as fd:
            string = fd.read()
        print(string, end='')
    except (ModuleNotFoundError, NameError, IOError, EnvironmentError):
        print("An issue occured with the program.")


if __name__ == "__main__":
    program()
