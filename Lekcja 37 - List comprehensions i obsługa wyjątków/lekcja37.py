# 1. Kwadraty licz od 1 do 10
lista_1 = [x**2 for x in range(1,11)]
print(lista_1) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 2. Każdy element listy dzielimy przez 2
lista_2 = [a//2 for a in lista_1]
print(lista_2)


# 3. Elementy podzielne przez 5 z zakresu od 1 do 34
lista_3 = [i for i in range(1,35) if i % 5 == 0]
print(lista_3)



# Ćwiczenie 1
# Masz listę punktów zdobytych przez graczy.
# Stwórz nową listę, w której każdy wynik będzie powiększony o 10 punktów bonusu.
punkty = [5, 12, 8, 20, 3]
cw_1 = [i+10 for i in punkty]
print(cw_1)

# wynik:
# [15, 22, 18, 30, 13]


# Ćwiczenei 2
# Masz listę wyników z quizu.
# Stwórz listę tylko z tych wyników, które są większe lub równe 50.
wyniki = [20, 75, 40, 90, 55, 10]
cw_2 = [g for g in wyniki if g >= 50]
print(cw_2)
# wynik:
# [75, 90, 55]




# Inne struktury
lista = [1,2,3,4,5,6,7,8,9,9]

# Zbiór (set comprehension)
zbior_1 = {i**2 for i in lista}
print(zbior_1)

# Krotka (generator)
krotka_1 = (i**2 for i in lista)
print(krotka_1)

# * GENERATOR - leniwa lista: 
# - nie tworzy wszystkich wyników od razu 
# - nie trzyma ich w pamięci 
# - generuje kolejne wartości „na żądanie” 
# - da się po nim iterować 

# Słownik (dict comprehension)
slownik_1 = {i : i**2 for i in lista}
print(slownik_1)

# -------------------------------------------
print("\n\n\n\n")


# ĆWICZENIA 
# 1️. Napisz funkcję dzielenie i mnożenie przyjmującą dwie wartości a i b,  
# która wyświetli wynik działania a/b i a*b.  
# Co się wydarzy jeżeli nie zaimplementujemy obsługi wyjątków  
# i spróbujemy dzielić przez 0? 

def dzialania(a, b):
    try:
        a/b
    except Exception as e:
        print(e)
    else:
        print(f"Wynik dzielenia {a} / {b} = {a/b}")
    finally:
        print(f"Wynik mnożenia {a} * {b} = {a*b}\n")

dzialania(5, 0)
dzialania(0, 5)
dzialania(5, 5)


# WŁASNE WYJĄTKI - RAISE 
# „Tutaj coś jest nie tak → przerwij normalne działanie i zgłoś błąd”. 
 
# raise Exception("komunikat") 
 
# własne wyjątki: 
# - za długa nazwa, 
# - dane złych typów, 
 
# Stwórzmy funkcję 'parzyste' która przyjmuje dwa argumenty 
# i je do siebie dodaje jeżeli oba są parzyste.  
# Jeżeli chociaż jeden z argumentów jest nieparzysty funkcja 
# powinna podnieść wyjątek. 

def parzyste(a, b):
    try:
        if a%2!=0 or b%2!=0:
            raise Exception("To nie są liczby parzyste.")
    except Exception as e:
        print(e)
    else:
        print(a+b)

parzyste(2,4) # 6
parzyste(1,6) # To nie są liczby parzyste.
parzyste(6,7) # To nie są liczby parzyste.