# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 2

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-25"


class Intern:
    """Notre class intern"""

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        """La classe Coffee"""

        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    unamed = Intern()
    mark = Intern('Mark')
    print("name:", unamed)
    print("name:", mark)
    print("coffee:", mark.make_coffee())
    try:
        print("work:", unamed.work())
    except Exception as e:
        print("except:", e)
