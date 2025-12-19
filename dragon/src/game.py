"""
Stwórz smoka o nazwie "Wawelski"
>>> dragon = Dragon('Wawelski')

Stworzenie smoka bez nazwy podnosi błąd
>>> dragon = Dragon()
Traceback (most recent call last):
    ...
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

Smok przy tworzeniu ma losowe punkty życia

Ustaw inicjalną pozycję smoka na x=50, y=100

Pobierz aktualną pozycję

Ustaw nową pozycję smoka na x=10, y=20

Przesuń smoka w lewo o 10 i w dół o 20

Przesuń smoka w lewo o 10 i w prawo o 15

Przesuń smoka w prawo o 15 i w górę o 5

Przesuń smoka w dół o 5

Smok zadaje obrażenia (losowo 5-20)

Zadaj 10 obrażeń smokowi

Zadaj 20 obrażeń smokowi

Zadaj 30 obrażeń smokowi

Zadaj 40 obrażeń smokowi

Zadaj 50 obrażeń smokowi

"""

import unittest


class Dragon:
    def __init__(self, name: str, /) -> None:
        self.name = name



class DragonTest(unittest.TestCase):
    def test_init_name_positional(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.name,  "Wawelski")

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            dragon = Dragon(name="Wawelski")  # noqa

    def test_init_no_name(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa