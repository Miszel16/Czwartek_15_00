# NumPy - Numerical Python

# - tablice wielowymiarowe (miacierze) [ndarray = N-Dimensional Array]
# - dużo złożonych funkcji matematycznych
# - operacje na duzych zbiorach danych
# - szybkość - zoptymalizowane operacje (oparte na językach niższego poziomu)
# - !tablice szybsze od list!

import numpy as np

# Zadanie 1
# Stwórz funkcję print_array() w której zaimplementowana zostanie dwuwymiarowa
# tablica oraz wyświetlone zostaną:
# a)Tablica    [[-1,   2,  -3] 
#               [ 4,   5,   6]
#               [ 7,   8,   9]]

# b)Pierwszy element tablicy
# c)Pierwszy zagnieżdżony element tablicy
# d)Typ utworzonego obiektu
# e)Kształt utworzonego obiektu
# Funkcja powinna zwracać utworzoną tablicę.

def print_array():
    tablica = np.array([[-1,   2,  -3], [ 4,   5,   6], [ 7,   8,   9]])
    print(f"Tablica: {tablica}")
    print(f"Pierwszy wiersz:\n {tablica[0]}")
    print(f"Pierwszy element: {tablica[0][0]}")
    print(f"Typ: {type(tablica)}")
    print(f"Kształt: {tablica.shape}")

    print(f"Wymiary: {tablica.ndim}")
    print(f"Liczba elementów: {tablica.size}")
    print(f"Typ danych: {tablica.dtype}")
    return tablica

arr = print_array()


# ------------------------------------------------------------------------------------
# Zadanie 2
# Stwórz funkcję shapeshifter która przyjmuje jako argument utworzoną wcześniej
# tablicę. 
# Funkcja powinna:
# a)Zmienić rozmiar tablicy na 9x1
# b)Zmienić rozmiar tablicy na 1x9
# c)Zmienić rozmiar tablicy na 3x3
# d)Zmienić rozmiar tablicy na -1x9
# e)Zmienić rozmiar tablicy na 3x-1
# f)Podzielić tablicę na 3 nowe tablice

def shapeshifter(tablica):
    print(f"Rozmiar  9 x 1:\n {tablica.reshape(9,1)}")
    print(f"Rozmiar  1 x 9:\n {tablica.reshape(1,9)}")
    print(f"Rozmiar  3 x 3:\n {tablica.reshape(3,3)}")
    print(f"Rozmiar -1 x 9:\n {tablica.reshape(-1, 9)}")
    print(f"Rozmiar  3 x-1:\n {tablica.reshape(3, -1)}")

    print("="*40)
    new_arr = np.array_split(tablica.reshape(-1,3), 3)
    print(new_arr)

shapeshifter(arr)

# ------------------------------------------------------------------------------------
# Zadanie 3
# Utwórz funkcję sortder_ndarray w której utworzona zostanie tablica, a następnie
# wyświetlona, oraz posortowana i ponownie wyświetlona.

def sorted_ndarray():
    tablica = np.array([[5,3,6], [3,7,8], [9,0,9]])
    print(f"Przed sortowaniem:\n {tablica}")
    print(f"Po sortowaniu:\n {np.sort(tablica)}")


sorted_ndarray()


# ------------------------------------------------------------------------------------
# Zadanie 4
# Stwórz funkcję generate_random_numbers która wygeneruje 10 losowych liczb
# całkowitych od 0 do 100, oraz 10 losowych liczb typu float z zakresu od 0 do 1.

print("="*40)

from numpy import random

def generate_random_numbers():
    for _ in range(10):
        print(random.randint(100))
    
    for _ in range(10):
        print(random.rand())

generate_random_numbers()


tablica1 = random.randint(50, size=(3,4))
print(tablica1)

tablica2 = random.rand(3,3)
print(tablica2)