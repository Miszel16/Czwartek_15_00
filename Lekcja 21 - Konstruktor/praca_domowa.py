# PRZYPOMINAJKA

# 1. Co to jest konstruktor?
# 🔹Konstruktor to specjalna metoda klasy w Pythonie o nazwie __init__,
#     która jest wywoływana automatycznie w momencie tworzenia obiektu.
# 🔹Służy do inicjalizacji atrybutów obiektu, czyli nadania im początkowych wartości.
# 🔹Jeśli nie napiszemy własnego konstruktora, Python automatycznie utworzy domyślny
#     konstruktor bezargumentowy, który po prostu tworzy pusty obiekt bez żadnej dodatkowej logiki.


# 2. Kiedy wywołuje się konstruktor?
# 🔹Konstruktor wywołuje się automatycznie przy tworzeniu obiektu klasy

# 3. Jakie sa rożnice pomiędzy zmienną klasy a obiektu?
# 🔹Zmienna klasy:
    # należy do całej klasy,
    # jest wspólna dla wszystkich obiektów,
    # zmiana jej wartości wpływa na wszystkie instancje,
    # przykład: Samochod.licznik1.

# 🔹Zmienna obiektu (instancji):
    # należy do konkretnego obiektu,
    # każdy obiekt ma własną kopię,
    # zmiana w jednym obiekcie nie wpływa na inne,
    # przykład: auto1.licznik2, auto2.licznik2.


# ------------------------------------------------------------------------------------
# Zadanie 1
# Celem zadania jest stworzenie 2 klas: Kolo i Kwadrat.
# Klasy mają być odpowiedzialne za przechowywanie odpowiednich dla danej figury
# geometrycznej wymiarów oraz posiadać metody wyświetlające pole i obwod tych figur.
# Następnie tworzymy po dwa obiekty dla każdej klasy i wyświetlamy ich pola i obwody

# Kolo 
# - konstruktor (promien)
class Kolo():
    def __init__(self, promien):
        self.promien = promien


# Prostokat 
# - konstruktor (boka, bokb)
class Protokat():
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b


# ------------------------------------------------------------------------------------
# Zadanie 2 „Pieski w schronisku”
# Stwórz klasę "Pies", która posiada:
# - atrybut klasy zliczający wszytskie obiekty (psiaki)
# - konstruktor tworzący obiekty (psiaki) i nadający obiektom atrybuty: imie, rasa
# - metode "przedstaw_sie", która za pomoca 'return' zwróci opis psiaka

# Następnie utwórz 3 obiekty i wywołaj metodę przedstaw_sie() dla każdego z nich
# Wypisz na końcu wartość atrybutu klasowego, który powinien zliczać wszytskei obiekty 



# ------------------------------------------------------------------------------------
# Zadanie 3 „Gra – Wojownicy”

# Stwórz klasę „Wojownik”, która posiada:
# - atrybut klasy domyslna_sila = 10
# - atrybut klasy zliczający wszystkich wojowników
# - konstruktor tworzący obiekty i nadający im atrybuty: imie oraz energia (na start 100)
# - metodę „atakuj”, która:
#         - zmniejsza energię o 10
#         - za pomocą return zwraca tekst: "<imie> atakuje z siłą <domyslna_sila>. Energia: <energia>"
# Następnie:
# 1. Utwórz 2 wojowników.
# 2. Niech każdy zaatakuje 2 razy.
# 3. Zmień wartość Wojownik.domyslna_sila = 25.
# 4. Niech znów zaatakują.
# 5. Wypisz liczbę wszystkich wojowników.



# ------------------------------------------------------------------------------------
# Zadanie 4 „Kanapka”

# Stwórz klasę „Kanapka”, która posiada:
# - konstruktor tworzący obiekt i nadający mu atrybuty: chleb, dodatek, sos
# - metodę „opis”, która za pomocą return zwróci tekst: „Kanapka: chleb = ..., dodatek = ..., sos = ...”
# - metodę „zmien_sos”, która przyjmuje nowy sos i zmienia self.sos
# - metodę „czy_jest_wege”, która zwraca True jeśli dodatek to np. "ser" lub "warzywa", a False w przeciwnym razie
# Następnie utwórz 2 obiekty, wypisz opisy, zmień sos w jednej kanapce i sprawdź czy_jest_wege().

