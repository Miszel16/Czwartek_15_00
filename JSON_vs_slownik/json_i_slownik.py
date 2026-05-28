import pprint

student = {
    "name": "Trener Alicja",
    "age": 21
}

#---------------------------------------------------
# FORMAT JSON (JavaScript Object Notation)
# - lekki format wymiany danych,
# - łatwy do odczytu i zapisu dla ludzi
# - łatwy do interpretacji i generowania dla maszyn
# - format tekstowy
# - wymiana danych między serwerem a aplikacją


# PODOBIEŃSTWA
# - składają się z par klucz-wartość
# - mog,ą zawierać zagnieżdzone dane
# - bardzo łatwa zmiana słownik <-> JSON

# RÓŻNICE
# 1. Słownik: działa tylko w Pythonie
#    JSON: działa wszędzie
# 2. Słownik: używany wewnątrz programu.
#    JSON: używany do wysyłania danych między komputerami.
# 3. JSON trzeba zamienić na tekst i z powrotem (serializacja/deserializacja).

# ------------- SŁOWNIK ---------------
gra = {"nazwa_gry" : "CS",
       "data_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}

print(gra.get("nazwa")) # wartość/None
print(gra["nazwa_gry"]) # wartość/Błąd

# - iterowanie
# 1. po kluczach
for key in gra.keys():
    print(key)

# 2. po wartościach
for value in gra.values():
    print(value)

# 3. po parach klucz-wartosc
for item in gra.items():
    print(item)


# dodanie pary klucz-wartosc
gra.setdefault("PEGI", 18)
pprint.pprint(gra) # pary alfabetycznie


# Usuwanie
# 1. i zwaracanie wartości spod podanego klucza
deleted = gra.pop("wydawca")
print(f"\n\n {deleted}")
pprint.pprint(gra)

# 2. i zwracanie ostatniej pary klucz-wartość
print(f"\n\n {gra}")
last_item = gra.popitem()
print(f"{last_item}")
print(gra)

# 3. spod podanego klucza
del gra["gatunek"]
print(gra)

# 4. wszytskie (czyszczenie)
gra.clear()
print(gra)


# ============================================
# BIBLIOTEKA json
# ============================================
# Biblioteka json pomaga:
# - zamieniać obiekty Pythona na tekst w formacie JSON (serializacja),
# - zamieniać tekst JSON na obiekty Pythona (deserializacja).
#
# To jest potrzebne np. gdy:
# - zapisujemy dane do pliku,
# - wysyłamy dane przez internet (np. do API),
# - chcemy, żeby inne programy mogły odczytać nasze dane.


# --------------------------------------------
# PODSTAWOWE FUNKCJE BIBLIOTEKI json
# --------------------------------------------
# 1. json.dumps()  [python -> JSON]
#    - zamienia obiekt Pythona (np. słownik) na łańcuch znaków (string)
#      w formacie JSON.
#
# 2. json.loads()   [JSON -> python]
#    - zamienia łańcuch znaków w formacie JSON na obiekt Pythona
#      (np. słownik).
#
# 3. json.dump()   [python -> JSON  PLIK!!!]
#    - zapisuje obiekt Pythona do pliku w formacie JSON.
#
# 4. json.load()   [PLIK!!! JSON -> python]
#    - wczytuje dane JSON z pliku i zamienia je na obiekt Pythona.
# --------------------------------------------

