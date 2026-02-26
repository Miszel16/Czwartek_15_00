class Samochod():
    # atrybuty klasy
    licznik_1 = 0

    # -------------- KONSTRUKTOR ---------------------------------
    def __init__(self, predkosc, mocKM, marka_model, kolor, rok):
        # atrybuty obiektu
        self.predkosc = predkosc
        self.mocKM = mocKM
        self.marka_model = marka_model
        self.kolor = kolor
        self.rok_produkcji = rok
        self.licznik_2 = 5

        # zmiana atrybutu_klasy
        Samochod.licznik_1 += 1
    # ------------------------------------------------------------

    def wyswietl(self):
        print(f"Model i marka: {self.marka_model}")
        print(f"kolor: {self.kolor}")
        print(f"rok produkcji: {self.rok_produkcji}")
        print(f"Max. prędkosć: {self.predkosc}")
        print(f"Moc w KM: {self.mocKM}")


print(Samochod.licznik_1) # 0

print("tworzymy auto")
auto1 = Samochod(480, 1500, "Bugatti chiron", "czarny", 2016)

print(Samochod.licznik_1) # 1
print(auto1.licznik_2) # 5
print(auto1.marka_model)

print("tworzymy auto")
auto2 = Samochod(250, 500, "toyota", "niebieska", 2014)
print(Samochod.licznik_1) # 2
print(auto2.licznik_2) # 5
print(auto2.marka_model)
