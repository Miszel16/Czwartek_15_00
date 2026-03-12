# PLAN
# - klasa bazowa: Postac  +
#       - konstruktor (nazwa, zycie, max_zycie) +
#       - metoda atakuj (obrazenia losowe) +

# - klasa pochodna: Gracz (konstruktor)
#       - metoda odpocznij +
#       - metoda walki

# - klasa pochodna: Przeciwnik (konstruktor, ["zombie", "szkielet", "ork", "Czarodziej z dalekiej krainy"])

from random import randint, choice

class Postac():
    def __init__(self, nazwa, zycie):
        self.nazwa = nazwa
        self.zycie = zycie # aktualne zycie
        self.max_zycie = zycie # maksymalne
    
    def atakuj(self, przeciwnik: "Postac"):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń.")
            przeciwnik.zycie -= atak

class Przeciwnik(Postac):
    def __init__(self, gracz):
        nazwa = choice(["Zombie", "Szkielet", "Ork", "Czarodziej z dalekiej krainy"])
        zycie = randint(1, gracz.max_zycie)
        # uruchomienie konstruktora klasy bazowej
        super().__init__(nazwa, zycie)


class Gracz(Postac):
    def __init__(self):
        nazwa = input("Podaj nazwę gracza: ")
        super().__init__(nazwa, 10)
    
    def odpocznij(self):
        if self.zycie < self.max_zycie:
            self.zycie += 1
        print(f"{self.nazwa} odpoczywa: życie: {self.zycie}/{self.max_zycie}")
    

    def walka(self, przeciwnik):
        walka = True
        while walka:
            print()
            print(f"życie {self.nazwa}: {self.zycie}")
            print(f"życie {przeciwnik.nazwa}: {przeciwnik.zycie}")

            akcja = input("Akcja (atak/uciekaj): ")

            if akcja == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                    return True
                else:
                    przeciwnik.atakuj(self)
                
            elif akcja == "uciekaj":
                przeciwnik.atakuj(self)
                print(f"życie gracza: {self.zycie}")
                print(f"{self.nazwa} ucieka.")
                walka = False
            
            else:
                print("Nieznana akcja.")
            
            if self.zycie <= 0:
                print(f"{self.nazwa} ginie przez {przeciwnik.nazwa}")
                return False
        return True


gracz = Gracz()
gra = True
while gra:
    akcja = input("Akcja (zwiedzaj/odpocznij): ")

    if akcja == "zwiedzaj":
        if randint(0,1) == 0:
            print(f"{gracz.nazwa} znalazł jaskinię!")
        else:
            przeciwnik = Przeciwnik(gracz)
            print(f"{gracz.nazwa} natrafia na {przeciwnik.nazwa}")
            gra = gracz.walka(przeciwnik)

    elif akcja == "odpocznij":
        gracz.odpocznij()
    else:
        print("Nieznana akcja")