# !/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exercice 3

"""

__auteur__ = "g.isaac@groupecerco.com"
__date__ = "2020-02-25"


class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self):
        return ("Just some hot water in a cup.")

    def __str__(self):
        return (
            "name : %s\n"
            "price : %.2f\n"
            "description : %s"
            % (self.name, self.price, self.description())
        )


class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"

    def description(self):
        return("A coffee, to stay awake.")


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"

    def description(self):
        return("Chocolate, sweet chocolate...")


class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"

    def description(self):
        return("Un po’ di Italia nella sua tazza!")


if __name__ == "__main__":
    for i in [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]:
        print(i, "\n")
