# Klasa -> obiekt(atrybuty)
# Klasa - szablon
# Obiektem 

# KLASA: Osoba(imie, nazwisko, wiek)
# OBIEKTY:
# (Martyna, XYZ, 15)
# (Nikodem, ABC, 12)

class Obozowicz():
    # atrybuty
    imie = ""
    nazwisko = ""
    wiek = 0

    # metody
    def czy_jest_pelnoletni(self):
        x = 18
        if self.wiek >= x:
            print(f"Osoba {self.imie} {self.nazwisko} jest pełnoletnia.")
        else:
            print(f"Osoba {self.imie} {self.nazwisko} nie jest pełnoletnia.")
    

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek


