# Zagadnienie 1 - Generowanie ciągu znaków
# Napisz program, który z ciągu w formacie: napis, liczba wygeneruje ciąg
# znaków. W wygenerowanym ciągu każdy napis powinien zostać powtórzony tyle
# razy ile wskazuje liczba go poprzedzająca.

#                        kot3ala3c11 -> kotkotkotalaalaalaccccccccccc

# Załóż, że dane zawsze zostaną dostarczone w
# prawidłowym formacie.

# ----------------------------------------------------------------------------------------

# Zagadnienie 2 - Znajdź pierwszy unikalny znak w sekwencji znaków
# Napisz program który znajdzie pierwszy unikalny znak w podanej
# sekwencji znaków. 
#             “ala ma kota, kot jest ali” -> “m”.

# ----------------------------------------------------------------------------------------

# Zagadnienie 3 - Funkcje anonimowe
# Zaimplementuj program, który sortuje listę liczb w oparciu o wartość ich
# kwadratów (liczba podniesiona do potęgi drugiej). Na przykład, dla listy [3, -2, 5,-4],
# jej kwadraty to [9, 4, 25, 16], a wynikowa lista po sortowaniu to [-2, 3, -4, 5].

# ----------------------------------------------------------------------------------------

# Zagadnienie 4 - zmienna liczba argumentów (*args, **kwargs)

# *args = „zbierz wszystkie podane wartości do jednej krotki”
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2)) #3
print(sum_numbers(1,2,3,4)) #10


# **kwargs = „zbierz wszystkie argumenty nazwane do słownika”
def osoba_zwyczajna(imie, nazwisko, wiek):
    print(imie, nazwisko, wiek)

osoba_zwyczajna(imie="Ania", nazwisko="Kowalska", wiek=20)

def osoba(**kwargs):
    print(kwargs)

osoba(imie="Kasia", nazwisko="Kowalska", wiek=20, wzrost=150)
osoba(nazwisko="belka", rod='orzel')



# razem 
def funkcja(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

funkcja(1,2,"kot",imie="zosia", wiek=20)

# Napisz program przedstawiający postać z gry RPG. Program powinien wypisać
# nazwę postaci składającą się z dowolnej liczby imion i przydomków podanych
# do funkcji jako argumenty nienazwane oraz dowolną liczbę klas (np. 'Wojownik', 'Mag') 
# wraz z ich poziomami, które zostaną przekazane do funkcji jako argumenty nazwane.

def create_hero(*args, **kwargs):
    name = " ".join(args)
    classes = "\n".join(f"Klasa: {k}, lvl: {l}" for k, l in kwargs.items())

    description = f"Bohater: {name}\n{classes}"
    print(description)

create_hero("Potężny", "Władca", "Ognia", Paladyn=50, Mag=20, Lucznik=5)









# ----------------------------------------------------------------------------------------

# Zagadanienie 5 - generatory
# Napisz program, który stworzy generator generujący liczby od 0 do podanej
# wartości (parametru limi) z krokiem 1. Utwórz dwa obiekty tego generatora z
# parametrem limit równym 5 i wywołuj je asynchronicznie (na zmianę).

# ----------------------------------------------------------------------------------------

# Zagadnienie 6 - dekoratory
# „opakowuje” funkcję dodatkowym zachowaniem
# Utwórz funkcję add(a,b) która czeka jedną sekundę a następnie wyświetla
# wynik dodawania liczb a i b. Utwórz dekorator @timeline który wyświetli czas
# wywołania funkcji oraz czas zakończenia jej pracy.