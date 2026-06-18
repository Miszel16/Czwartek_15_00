slownik = {
    "klucz": "wartość",
    "klucz2": 2
}

# KROTKA (tuple)
# - stała
# - współrzedne (x, y)

krotka = (4,2,11,2,3,4)
print(krotka, type(krotka))
krotka_2 = (4,)
print(krotka_2, type(krotka_2))

# lista = [1,2,3]
# print(lista[0])
print(krotka[0]) # 4

print(krotka[1:4]) # 2,11,2


# METODY KROTKI
# [.count()] - zliczanie wystąpień wartości
ile = krotka.count(2)
print(f"Ile '2' w krotce: {ile}")

# [.index()] - pierwsze wystąpienei wartości
indeks = krotka.index(2)
print(f"Indeks pierwszej '2': {indeks}")


print("ZBIORY:\n")
# ZBIÓR (set)
# - nie ma duplikatów
# - wszytsko wrzucone do worka
zbior = {1,2,3,4,4,4,4,4,4,4}
print(zbior, type(zbior))

pusty_zbior = set()
print(pusty_zbior, type(zbior))

# METODY ZBIORÓW
# 1. Dodanie do zbioru [.add()]
zbior.add(7)
print(zbior) # 1,2,3,4,7

# 2. Usunięcie elementu o danej wartości [.remove()]
zbior.remove(1)
print(zbior) # 2,3,4,7
# - jeśli nie ma wartosci to wyrzuca błąd


# 3. Usunięcie elementu o danej wartości jeżeli istnieje [.discard()]
zbior.discard(9)
print(zbior) # 2,3,4,7

# 4. Usunięcie pierwszego 'losowego' elementu i zwrócenie [.pop()]
element = zbior.pop()
print(element, zbior)

# 5. Czyszczenei zbioru [.clear()]
zbior.clear()
print(zbior)


# ----------------- KONWERSJE ------------------
print("\n\n\n")
zbior = {1,2,3} # set
krotka = (4,5,6) # tuple
lista = [7,8,8,9] # list

# 1. Konwersja na liste
zbior_do_listy = list(zbior)
print(zbior_do_listy, type(zbior_do_listy))

krotka_do_listy = list(krotka)
print(krotka_do_listy, type(krotka_do_listy))


# 2. Konwersja na krotke
zbior_do_krotke = tuple(zbior)
print(zbior_do_krotke, type(zbior_do_krotke))

lista_do_krotki = tuple(lista)
print(lista_do_krotki, type(lista_do_krotki))


# 3. Konwersja na zbiór
lista_do_zbioru = set(lista)
print(lista_do_zbioru, type(lista_do_zbioru))

krotki_do_zbioru = set(krotka)
print(krotki_do_zbioru, type(krotki_do_zbioru))