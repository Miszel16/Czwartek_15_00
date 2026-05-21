# Algorytm 

# Lista wygenerowania do testowania
# - 20 losowych elementów (1-100)
import random
import pprint

moja_lista = []

for i in range(20):
    l = random.randint(1, 100)
    moja_lista.append(l)

print(moja_lista)

# ------------------------------------------------------------------------
# Słownik - krótko

x = [1,2,3,4]

osoba = {
    "imie": "Alicja",
    "wiek": 21,
    "doroslosc": True,
    "adres": {
        "miasto": "Poznan",
        "ulica": "XYZ",
        "numer": 10
    }
}


# # ----------------- OPERACJE NA SŁOWNIKACH -----------------
# - dodanie nowej pary klucz - wartość:
osoba["email"] = "xxx.yyyy@gmail.com"
pprint.pprint(osoba)

# - usunięcie pary klucz-wartość:
del osoba["doroslosc"]
pprint.pprint(osoba)


# - dostęp do wartości na podstawie klucza:
print(osoba["adres"])


# - iteracja przez pary klucz-wartość w słowniku:
for klucz, wartosc in osoba.items():
    print(klucz, wartosc)


print("\n\n\n\n\n")
# ------------------------------------------------------------------------
# 1. SORTOWANIE BĄBELKOWE (bubble sort) O(n*n)
# wizualizacja:
# https://commons.wikimedia.org/wiki/File:Bubble-sort.gif
# https://www.sortvisualizer.com/bubblesort/


def bubble_sort(lista):
    n = len(lista)
    for i in range(n): # i = 0
        for j in range(0, n-1-i):
            # porównanie elemntów
            if lista[j] > lista[j+1]:
                # zamiana elementów
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

print(f"Nieposortowana lista: {moja_lista}")
print(f"Posortowana lista: {bubble_sort(moja_lista)}")


# 4 3 2 1  (4)
# 0 1 2 3 - indeksy


#i = 0
# 3 4 2 1   I

# 3 2 4 1  II

# 3 2 1 4  III
# ---------------------------
#i = 1
# 2 1 3 4


# ------------------------------------------------------------------------

# 2. WYSZUKIWANIA

# 2.1 WYSZUKIWANIE LINIOWE
# - jak sprawdzić czy dana wartość znajduje się w naszej liście? 

def linear_search(lista, x):
    n = len(lista)
    for i in range(n): # start, stop, step  (0, 1, 2, 3, 4, 5)
        if lista[i] == x:
            return i # numer indeksu
    
    return -1

print(linear_search(moja_lista, 7))

# 4 3 2 5 4 3  n = 6   x = 5
# 0 1 2 3 4 5  i



# 2.2 WYSZUKIWANIE BINARNE
# - działa na posortowanym zbiorze !!!!!!!
# - metoda dziel i zwyciężaj
# https://www.mathwarehouse.com/programming/gifs/binary-vs-linear-search.php

def binary_search(lista, x):
    low = 0
    high = len(lista)-1
    mid = 0
    while low <= high:
        # wyliczamy środek
        mid = (high + low)//2

        if lista[mid] == x:
            return mid
        
        elif lista[mid] < x:
            low = mid + 1

        elif lista[mid] > x:
            high = mid - 1
    return -1


moja_lista = [1,2,3,4,4,4,4,4,4,4,7]
print(f"Wyszukiwanie binarne: {binary_search(moja_lista, 7)}")







# ------------------------------------------------------------------------
# ZADANIA DODATKOWE
# ZADANIE 1
# Zadaniem ucznia jest stworzenie programu, który będzie działał jak książka
# telefoniczna. Program powinien mieć następujące funkcjonalności:

#   ● Dodawanie nowego kontaktu - program powinien pytać użytkownika o imię i
#   nazwisko oraz numer telefonu i dodać te dane do listy kontaktów. Lista
#   kontaktów powinna być przechowywana w postaci listy słowników, gdzie
#   każdy słownik reprezentuje jeden kontakt.

#   ● Sortowanie kontaktów za pomocą metody sortowania bąbelkowego -
#   program powinien sortować listę kontaktów alfabetycznie według nazwisk z
#   wykorzystaniem funkcji bubble_sort.

#   ● Wyświetlanie listy kontaktów - program powinien wyświetlić listę kontaktów
#   w formacie: "imię nazwisko - numer telefonu". Kontakty powinny być
#   posortowane alfabetycznie według nazwisk.









# ------------------------------------------------------------------------

# ZADANIE 2
# Zadaniem ucznia jest napisanie programu, który losuje liczbę z zakresu od 1 do
# 100, a następnie komputer będzie zgadywał tę liczbę, a my będziemy mu udzielać
# podpowiedzi w postaci "za mało" lub "za dużo" w zależności od tego, czy
# zgadnięta liczba jest mniejsza czy większa od wylosowanej liczby.

# Komputer będzie korzystał z algorytmu binary search, a program zakończy się, gdy
# komputer zgadnie liczbę.

# * Rekurencja - proces wywoływania funkcji przez samą siebie. 
# 
# W tym konkretnym kodzie, funkcja binary_search można zastosować rekurencje.
# Funkcja sortowania binarnego może być rekurencyjna
# będzie wywoływać samą siebie w dwóch warunkach:
# - kiedy odpowiedź jest "za mało",
# - kiedy odpowiedź jest "za dużo".
# Proces rekurencyjny trwa tak długo, aż odpowiedź jest "tak",
# wtedy funkcja zwraca wartość guess.












# ------------------------------------------------------------------------
# PODSUMOWANIE:
#   ● Wyszukiwanie binarne - podziaŁ uporządkowanej listy na połowy i
#   iteracyjnE przeszukiwaniE jednej z nich w poszukiwaniu szukanej wartości.

#   ● Sortowanie bąbelkowe - porównywaniE sąsiednich elementów listy
#   i zamianie ich kolejności, jeśli są w niewłaściwej kolejności.

# Pytania powtórzeniowe:
#   ● W jaki sposób działa wyszukiwanie binarne?
#   ● Jak działa sortowanie bąbelkowe?