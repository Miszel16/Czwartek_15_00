# 1. Zadanie - Problem
# Program, zapisów na obóz
#   - Zapisze dane czterech osób (imiona, nazwiska i wiek).
#   - Wypisze ich imię i nazwisko.
#   - Sprawdzi, czy dana osoba jest pełnoletnia (wiek ≥ 18),
#     czy niepełnoletnia, i wypisze odpowiedni komunikat.
#     (Jeśli funkcja to musimy przekazywać wszytskie zmienne)
# "Osoba *imie* *naziwkso* jest/nie jest pełnoletnia"

imie1 = "Martyna"
nazwisko1 = "XYZ"
wiek1 = 15

imie2 = "Nikodem"
nazwisko2 = "ABC"
wiek2 = 12

imie3 = "Bogumił"
nazwisko3 = "GHJ"
wiek3 = 53

imie4 = "Lena"
nazwisko4 = "PKL"
wiek4 = 18

print(imie1, nazwisko1)
if wiek1 >= 18:
    print(f"Osoba {imie1} {nazwisko1} jest pełnoletnia.")
else:
    print(f"Osoba {imie1} {nazwisko1} nie jest pełnoletnia.")


print(imie2, nazwisko2)
if wiek2 >= 18:
    print(f"Osoba {imie2} {nazwisko2} jest pełnoletnia.")
else:
    print(f"Osoba {imie2} {nazwisko2} nie jest pełnoletnia.")


print(imie3, nazwisko3)
if wiek3 >= 18:
    print(f"Osoba {imie3} {nazwisko3} jest pełnoletnia.")
else:
    print(f"Osoba {imie3} {nazwisko3} nie jest pełnoletnia.")


print(imie4, nazwisko4)
if wiek4 >= 18:
    print(f"Osoba {imie4} {nazwisko4} jest pełnoletnia.")
else:
    print(f"Osoba {imie4} {nazwisko4} nie jest pełnoletnia.")


# Klasa - szablon
# Obiektem 

# KLASA: Osoba(imie, nazwisko, wiek)
# OBIEKTY:
# (Martyna, XYZ, 15)
# (Nikodem, ABC, 12)
