# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 1

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-25"

from settings import *
import sys
from re import *


def ecriture():
    """prend un fichier .template et remplace dans celui-ci les valeurs entre {} par celles 
indiquées dans le fichier settings.py"""

    if len(sys.argv) != 2:
        print("Usage: render.py <file>.template ")
        sys.exit(0)

    filename = sys.argv[1]
    try:
        if match("\w+.template", filename):
            with open(filename, 'r') as f:
                contenu = f.read()
                a_ecrire = contenu.format_map(globals())
                file_html = filename.replace('.template', '.html')

            with open(file_html, 'w') as f_h:
                f_h.write(a_ecrire)
        else:
            print(f"Le fichier {filename} n'a pas .template comme extension.")
            sys.exit(0)

    except FileNotFoundError as e:
        print(f"Le fichier {e.filename} n'existe pas.")
        sys.exit(0)
    except PermissionError as e:
        print(f"Droits de lecture absent sur le fichier{e.filename}")
        sys.exit(0)
    except Exception as e:
        print("Une erreur a empeché l'ouverture du fichier.".format(e))
        sys.exit(0)


if __name__ == '__main__':
    ecriture()
