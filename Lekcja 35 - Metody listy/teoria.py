lista = [1,2,3,4,5,6,7,8,9,10]

# for i in range(1,10,2): # 1 3 5 7 9
#     print(lista[i])


# for i in range(0, len(lista), 2):
#     print(lista[i])

# - indeksowanie (od przodu i od tyłu)
# - dodanie nowego elementu na koniec (.append)
# - dynamiczna
# - przechowywanie różnych typów


moja_lista = [16, "kot", 7.5, 13, True]

# METODY
# --------------------------------------------------------------
# 1) dodawanie lementu na koniec listy
# "Niedziela"
moja_lista.append("Niedziela")
print(f"{moja_lista}\n")

# --------------------------------------------------------------
# 2) poszerzenie listy [.extend()]
zwierzeta = ["pies", "koń", "sarna", "zebra"]
moja_lista.extend(zwierzeta)
print(f"{moja_lista}\n")


# --------------------------------------------------------------
# 3) dodawanie pod wskazany indeks [.insert()]
print(f"{list(enumerate(moja_lista))}\n")

gra = "League of Legends"
moja_lista.insert(5, gra)

print(f"{list(enumerate(moja_lista))}\n")

# --------------------------------------------------------------
# 4) usuwanie elemntu o konkretnej wartości [.remove()] (tylko pierwszego)
# *
# moja_lista.append("Niedziela")
# moja_lista.append("Niedziela")
# print(f"{moja_lista}\n") # x3 Niedzila

# *
moja_lista.remove("Niedziela")
print(f"{moja_lista}\n")

# moja_lista.remove("Niedziela")
# print(f"{moja_lista}\n")

# --------------------------------------------------------------
# 5) usuwanie elemntów spod wskazanego indeksu i ZWRÓCENIE GO [.pop()]
print(f"{moja_lista}\n")
element = moja_lista.pop(1) # domyślnie usuwamy ostatni element
print(f"{moja_lista}\n")

# *
# element2 = moja_lista.pop(60) # domyślnie usuwamy ostatni element
# print(f"{moja_lista}\n")


# --------------------------------------------------------------
# 6) znajdywanie indeksu danej wartości [.index()]
print(f"{list(enumerate(moja_lista))}\n")

# I
id = moja_lista.index("League of Legends")
print(id)

# II
id = moja_lista.index("League of Legends", 4)
print(id)

# III
id = moja_lista.index("League of Legends",0, 5)
print(id)

# --------------------------------------------------------------
# 7) Zliczanie wystąpień [.count()]

ile = moja_lista.count("League of Legends")
print(f"Wystąpienia: {ile}")


# --------------------------------------------------------------
# 8) sortowanie [.sort()]

nowa_lista = [1,2,3,2,1,1,2,23,4]
print(f"{nowa_lista}\n")
nowa_lista.sort()
print(f"{nowa_lista}\n")


# --------------------------------------------------------------
# 9) odwrócenie kolenosci listy [.reverse()]
print(f"{moja_lista}\n")
moja_lista.reverse()
print(f"{moja_lista}\n")


# --------------------------------------------------------------
# 10) kopiowanie listy [.copy()]
# * kopiowanie płytkie  - PRACA DOMOWA
kopia_moja_lista = moja_lista.copy()
print(f"Moja_lista: {moja_lista}\n")
print(f"Kopia_moja_lista: {kopia_moja_lista}\n")

# --------------------------------------------------------------
# 11) Czyszczenie listy [.clear()]
moja_lista.clear()
print(f"Moja_lista: {moja_lista}\n")



# PRACA DOMOWA - ZADANIA
# Zadania 

# 1 Stwórz 2 listy składające się z 3 liczb każda
# 2 Połącz stworzone wcześniej listy
# 3 Usuń elementy z indeksami 2 i 5 , który element należy usunąć najpierw?
# 4 Usuń największą i najmniejszą liczbę z listy (zakładamy że nie znamy)
# 5 Dodaj liczbę do listy
# 6 Posortuj listę
# 7 Utwórz kopię listy
# 8 Odwróć kolejność elementów w kopii
# 9 Dodaj do każdej wartości w pierwszej listy 1, a w drugiej odejmij 1
# 10 Wyświetl obie listy