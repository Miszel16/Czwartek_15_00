```python
import re


# ============================================================
#                 PRACA DOMOWA — REGEX
# ============================================================
# Uzupełnij wszystkie miejsca oznaczone jako TODO.
#
# Nie zmieniaj tekstów testowych.
# Do każdego zadania napisz odpowiedni wzorzec regex.
# ============================================================


# ------------------------------------------------------------
# ZADANIE 1 — LICZBY CAŁKOWITE I DZIESIĘTNE
# ------------------------------------------------------------
# Znajdź wszystkie liczby znajdujące się w tekście.
#
# Liczby mogą:
# - być dodatnie lub ujemne,
# - być całkowite,
# - zawierać część dziesiętną oddzieloną przecinkiem lub kropką.
#
# Oczekiwany wynik:
# ['-5', '18.5', '22,75', '100']

tekst = """
Rano było -5 stopni. Po południu temperatura wzrosła
do 18.5 stopnia. Produkt kosztuje 22,75 zł, a klient
zapłacił banknotem 100 zł.
"""

wzorzec = r""  # TODO

liczby = re.findall(wzorzec, tekst)

print("\n" + "=" * 60)
print("ZADANIE 1")
print("Znalezione liczby:", liczby)


# ------------------------------------------------------------
# ZADANIE 2 — NAZWY WŁASNE
# ------------------------------------------------------------
# Znajdź wszystkie całe słowa zaczynające się wielką literą.
#
# Wzorzec powinien obsługiwać również polskie litery.
#
# Oczekiwany wynik:
# ['Alicja', 'Łukasz', 'Poznania', 'Żaneta', 'Olsztyna']

tekst = """
Alicja i Łukasz pojechali z Poznania.
Na miejscu spotkała ich Żaneta z Olsztyna.
"""

wzorzec = r""  # TODO

nazwy = re.findall(wzorzec, tekst)

print("\n" + "=" * 60)
print("ZADANIE 2")
print("Znalezione nazwy:", nazwy)


# ------------------------------------------------------------
# ZADANIE 3 — WALIDACJA KODU PRODUKTU
# ------------------------------------------------------------
# Sprawdź, czy kod produktu jest zapisany poprawnie.
#
# Poprawny kod składa się z:
# - dokładnie 3 wielkich liter,
# - myślnika,
# - dokładnie 4 cyfr,
# - myślnika,
# - jednej litery X, Y albo Z.
#
# Poprawne przykłady:
# ABC-1234-X
# KOT-0007-Z
#
# Niepoprawne przykłady:
# AB-1234-X
# abc-1234-X
# ABC-12345-Y
# kod ABC-1234-X

kod_produktu = input(
    "\n" + "=" * 60 +
    "\nZADANIE 3\nPodaj kod produktu: "
)

wzorzec = r""  # TODO

wynik = re.search(wzorzec, kod_produktu)

if wynik:
    print("Kod produktu jest poprawny.")
else:
    print("Kod produktu jest niepoprawny.")


# ------------------------------------------------------------
# ZADANIE 4 — CENZUROWANIE SŁÓW
# ------------------------------------------------------------
# Zamień każde wystąpienie słowa:
#
# słaby
# nudny
# beznadziejny
#
# na tekst:
#
# ***
#
# Wielkość liter nie powinna mieć znaczenia.
#
# Oczekiwany wynik:
# Ten film jest ***. Fabuła była ***, a zakończenie ***.

tekst = """
Ten film jest słaby. Fabuła była NUDNA, a zakończenie beznadziejne.
"""

wzorzec = r""  # TODO

ocenzurowany_tekst = re.sub(
    wzorzec,
    "***",
    tekst,
    flags=re.IGNORECASE
)

print("\n" + "=" * 60)
print("ZADANIE 4")
print(ocenzurowany_tekst)


# ------------------------------------------------------------
# ZADANIE 5 — DZIELENIE LISTY DANYCH
# ------------------------------------------------------------
# Podziel tekst na osobne elementy.
#
# Elementy mogą być oddzielone:
# - przecinkiem,
# - średnikiem,
# - pionową kreską,
# - dowolną liczbą spacji.
#
# Oczekiwany wynik:
# ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML']

tekst = "Python, Java;C++ | JavaScript,SQL   ;   HTML"

wzorzec = r""  # TODO

elementy = re.split(wzorzec, tekst)

print("\n" + "=" * 60)
print("ZADANIE 5")
print("Podzielone elementy:", elementy)


# ============================================================
#                    KONIEC PRACY DOMOWEJ
# ============================================================
```
