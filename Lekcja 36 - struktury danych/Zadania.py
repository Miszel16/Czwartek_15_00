#Zadania
# 1. Stwórz krotkę, listę, słownik i zbiór zawierający po 3 elementy
lista = [1,2,3]
slownik = {
    "klucz1" : 4,
    "klucz2" : 5,
    "klucz3" : 6
}
zbior = {7,8,9}
krotka = (10,11,12)


# 2. Za pomocą funkcji len() sprawdź długości poszczególnych obiektów
print(len(lista))
print(len(krotka))
print(len(zbior))
print(len(slownik))


# 3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów
print("Lista:")
for i in lista:
    print(i)

print("Krotka:")
for i in krotka:
    print(i)

print("Zbior:")
for i in zbior:
    print(i)

print("Słownik:")
for i in slownik:
    print(i)


# 4. Teraz wypisz wartości słownika zamiast kluczy
print("Słownik wartości:")
for i in slownik.values():
    print(i)


# 5. Wypisz te same elementy w odwrotnej kolejności, 
# czy zawsze jest to możliwe bezpośrednio?
# * podpowiedzi:
# - [start:stop:step] np. [::1] - wypisze wszystkie elementy
# - tylko struktury z indeksami można iterowac od końca (konwersja)



# 6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.



# 7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.



# 8. Sprawdź długość listy.



# 9.Zamień listę na krotkę- krotka2 i sprawdź jej długość.



# 10.Zamień krotkę na zbiór - zbior2 i sprawdź jego długość, z czego wynika różnica?