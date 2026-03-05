# DZIEDZICZENIE

# KLASA BAZOWA - NADRZĘDNA
class Zwierze():
    def __init__(self, imie, wiek, wysokosc, kolor):
        self.imie = imie
        self.wiek = wiek
        self.wysokosc = wysokosc
        self.kolor = kolor

    def jedz(self):
        print(f"{self.imie} je.")

    def wydaj_dzwiek(self):
        print(f"{self.imie} wydaje dźwięk")
    
# pies
zwierze1 = Zwierze("Azor", 5, 20, "biały")
zwierze1.jedz()
zwierze1.wydaj_dzwiek()


class Pies(Zwierze):
    def __init__(self, imie, wiek, wysokosc, kolor, rasa):
        # uruchamiany konstruktor klasy bazowej/nadrzędnej
        super().__init__(imie, wiek, wysokosc, kolor)
        self.rasa = rasa
    
    def wypisz_rase(self):
        print(f"{self.imie}: jest rasy {self.rasa}")


pies1 = Pies("Racuch", 4, 53, "jasny złoty", "Golden Retriever")
pies1.jedz()
pies1.wydaj_dzwiek()
pies1.wypisz_rase()


# ZADANIE
# 1. Stworzyć klasę Ptak dziedziczącą po klasie Zwierze, która ma mieć:
#    - konstruktor wywołujkący konstruktor klasy bazowej,
#    - metodę lec()
# 2. Stworzyć kolejną klasę Orzel, dziedziczącą po Ptak, która ma mieć:
#    - konstruktor wywołujkący konstruktor klasy nadrzędnej,
#    - metodę poluj(), w której wywołujemy metodę lec() z klasy nadrzędnej.
# 3. Następnie tworzymy obiekt klasy Orzel i wywołajmy wszystkie metody

#        klasa ptak
#             |
#             V
# klasa Sowa, klasa Orzel 