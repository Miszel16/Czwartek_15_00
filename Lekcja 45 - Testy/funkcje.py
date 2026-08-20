def add(a, b):
    return a + b #3 + 4 = 7

# Zadanie 1. Palindrom
# Napisz funkcję sprawdzającą czy dane słowo jest palindromem (palindrom to
# słowo które pisane od przodu i od tyłu jest identyczne).
# Napisz testy, które sprawdzą, czy słowa “kamilslimak” i “ala” są palindromami, a
# słowa “wiadro” i “kamyk” nimi nie są.

def is_palindrom(word):
    return word == word[::-1] # True / False



# Zadanie 6. Średnia z listy
# Napisz program (bez korzystania z funkcji mean) który policzy średnią wartość z
# listy. Program powinien zwrócić -1 jeżeli lista jest pusta oraz -2 jeżeli w liście
# znajdują się wartości nie będące liczbami.

def calculate_mean(list_of_numbers):
    if len(list_of_numbers) == 0:
        return -1

    for x in list_of_numbers:
        if type(x) != int:
            return -2
    
    mean = sum(list_of_numbers)/len(list_of_numbers)
    return mean

