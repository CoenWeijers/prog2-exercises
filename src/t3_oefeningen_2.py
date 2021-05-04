import math


def is_even(x):
    """Geef True als x even is, anders False"""
    elif   x==0
        return False
    elif x/3==0
         return "False"
    else: "True"
    return True


def is_oneven(x):
    """Geef True als x oneven is, anders False"""
    # Implementeer deze functie gebruik makend van is_even
    elif x == 1:
    return False

elif x/3 == 0
    return "False"
else: "True"
    return "True"



def volume_bol(r):
    """Return volume bol met straal r"""
    pi = 3,14
    result = 4/3*pi*r**3
    return result


def oppervlakte_cirkel(r):
    """Return oppervlakte cirkel met straal r"""
    # Deze functie kan je gebruiken om het volume van de donut te berekenen.
    pi = 3,14
    result = pi*r**2
    return result


def omtrek_cirkel(r):
    """Return omtrek cirkel met straal r"""
    # Deze functie kan je gebruiken om het volume van de donut te berekenen.
    pi = 3,14
    result = 2*pi*r
    return result


def volume_donut(r, R):
    """Return volume donut met straal r en R
    waarbij r de dikte van de donut is, en R
    de grootte van de donut.
    """
    pi = 3,14
    result =  2*pi**2*r**2
    return result


def stats(punten):
    """Return het gemiddelde, het maximum, het minimum en het aantal getallen
    als een lijst met punten gegeven werd."""

    getelde_punten = stats.count(punten)
    gemiddelde = getelde_punten/punten
    min_getallen = max(punten)
    max_getallen = min(punten)

    return 0


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        """Return de omtrek van de cirkel met straal r"""
        pi = 3, 14
        result = 2 * pi * r
        return result

        return 0

    def oppervlakte(self):
        """Return de oppervlakte van de cirkel met straal r"""
        pi = 3, 14
        result = pi * r ** 2
        return result
        return 0

    def __str__(self):
        """Return een string zoals aangegeven in de testen"""
        str(oppervlakte_cirkel(), omtrek_cirkel())
        return ""


def pythagoras(a, b):
    """Return de lengte van de schuine zijde als de lengtes
    van de rechthoekszijden gegeven zijn door a en b"""
    a = rechthoekzijde_een
    b = rechthoekzijde_twee
    result = (a**2 + b**2)**1/2
    return result


def is_palindroom(woord):
    """Return True als het omgekeerde van het woord gelijk
    is aan het woord zelf. Return anders False."""




    my_str = woord

    my_str = my_str.casefold()

    rev_str = reversed(my_str)

    if list(my_str) == list(rev_str):
        return True
    else:
        return False
