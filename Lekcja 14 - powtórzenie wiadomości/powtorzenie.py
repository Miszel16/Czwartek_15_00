# QUIZ
# https://quiz.giganciprogramowania.edu.pl/wdp-python1-q3

# Powtórka do quizu:
# 1. Type hinting
# 2. Argumenty funkcji:
#     - zapis argumentów przekazywanych do funkcji

# 3. Funkcja zwracająca wartość
#     - co to znaczy?
#     - słowo kluczowe #return

# 4. Pygame
#     - najważniejsze elementy


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Powtórka przed zadaniami:
# 1. Instrukcja warunkowa if-elif-elif-else
# 2. Pętla while 
# 3. Pętla for
#   - iterowanie - przejście element po elemencie
#   - range(start, stop, step)

# 4. Listy


# 5. Funkcje x
# 6. Type hinting x
# 7. Moduł pygame x





#-----------------------------------------------------------------------------
#                                   ZADANIA
#-----------------------------------------------------------------------------
# 1. Utwórz trzy zmienne, do których wpisz wartość 3 jako odpowiedni typ:
# - x_int - jako liczba całkowita
# - x_float - jako liczba z przecinkiem
# - x_str - jako napis

a = 3
b = 3.00
c = "3"

print(f"{a}  {type(a)}")
print(f"{b}  {type(b)}")
print(f"{c}  {type(c)}")



#-----------------------------------------------------------------------------
# 2. Utwórz zmienną napis_liczba, która przechowuje wartość "290".
# Utwórz zmienną x. Użyj konwersji z typu str na typ int, aby zmienna x
# przechowywała to co napis_liczba, ale jako typ liczby całkowitej

napis_liczba = "-290"
x = int(napis_liczba)
z = float(napis_liczba)

y = bool(napis_liczba) #True
pusty = ""
a = bool(pusty) # False
print(y)
print(a)




#-----------------------------------------------------------------------------
# 3. Utwórz 3 zmienne:
# - pole_trojkata
# - podstawa_trojkata
# - wysokosc_trojkata
# Do podstawa_trojkata oraz wysokosc_trojkata powinny trafić wartości odczytane z
# konsoli (od użytkownika).
# Oblicz pole takiego trójkąta i zapisz wynik w zmiennej pole_trojkata
# Wyświetl wynik jako komunikat:

# Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX
# Zamiast XX powinny pojawić się wartości liczbowe

def pole_trojkata():
    podstawa = float(input("Podaj podstawę trójkąta: "))
    wysokosc = float(input("Podaj wysokość trójkąta: "))

    pole = podstawa * wysokosc /2
    print(f"Pole trójkąta o podstawie {podstawa} oraz wysokości {wysokosc} wynosi {pole}")
    return pole

pole_trojkata()



#-----------------------------------------------------------------------------
# 4. Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli 
# jeden z komunikatów:
# - Jesteś pełnoletni/a
# - Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia
# Zamiast XX powinna pojawić się wartość liczbowa

wiek = int(input("Podaj wiek: "))

if wiek >= 18:
    print("Jesteś pełnoletni/a")
else:
    wynik = 18 - wiek
    print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {wynik} lat do 18 roku życia")




#-----------------------------------------------------------------------------
# 5. Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
# użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
# rozrywki i na tej podstawie obliczy koszt transakcji.
# Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):

# - 1 -> 50 zł   x
# - 2 -> 50 zł   x
# - 3 -> 100 zł
# - 4 -> 100 zł
# - 5 -> 200 zł
# - 6 -> 200 zł
# - 7 -> 250 zł
# - 8 -> 200 zł
# - 9 -> 200 zł
# - 10 -> 100 zł
# - 11 -> 100 zł
# - 12 -> 50 zł  x
# Wyświetl komunikat:
# "Cena biletów: XX zł"

# XX to wartość liczbowa

# Jeśli wprowadzono niepoprawny numer miesiąc program powinien wyświetlić
# informację:
# "Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"

liczba_biletow = int(input("Podaj liczbę biletów: "))
miesiac = int(input("Podaj miesiąc: "))

if miesiac == (1 or 2 or 12):
    print(f"Koszt to {50*liczba_biletow}")
elif miesiac == (3 or 4 or 10 or 11):
    print(f"Koszt to {100*liczba_biletow}")




#-----------------------------------------------------------------------------
# 6. Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na
# ekranie tyle wyników z rzutu kością sześcienną.
# Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).







#-----------------------------------------------------------------------------
# 7. Napisz funkcję, która przyjmuje 2 argumenty:
# - tekst, typu str
# - n, typu int
# a zwraca nowy napis, który powstaje poprzez połączenie text n razy.

# Szablon funkcji:
# def laczenie_slow(???) -> ???:
# nowy_tekst = ""
# ???
# ???
# return ???
# Zastąp wszystkie znaki zapytania odpowiednimi wyrazami/instrukcjami/itd





#-----------------------------------------------------------------------------
# 8. Przygotuj funkcję, która otrzymuje jeden argument: n - liczbę elementów.
# Funkcja ma zwrócić listę n - losowych elementów od 0 do 100
# Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości







#-----------------------------------------------------------------------------
# 9. Napisz program aplikacji graficznej, która co 2 sekundy zmienia kolor tła. Nowy
# kolor tła powinien być losowany.
# Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 2 sekundy
# Pamiętaj o budowaniu koloru RGB:
# RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
# RGB = [R, G, B] możesz przechowywać to jako listę
# Kolor startowy - biały (255,255,255)





#-----------------------------------------------------------------------------
# 10.Dodaj do swojego wykrywanie naciśnięcia klawisza 'b'.
# Jeśli taki klawisz zostanie naciśnięty kolor tła powinien zmienić się na czarny - po
# puszczeniu klawisza kolor:
# - powinien zostać na nowo wylosowany - wersja podstawowa
# - powinien wrócić poprzedni kolor - wersja rozszerzona