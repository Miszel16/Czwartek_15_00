#      plik              klasa
from Uzytkownicy import Obozowicz

obozowicz1 = Obozowicz()
obozowicz1.imie = "Martyna"
obozowicz1.nazwisko = "XYZ"
obozowicz1.wiek = 15

obozowicz2 = Obozowicz()
obozowicz2.imie = "Nikodem"
obozowicz2.nazwisko = "ABC"
obozowicz2.wiek = 12


obozowicz3 = Obozowicz()
obozowicz3.imie = "Bogumił"
obozowicz3.nazwisko = "GHJ"
obozowicz3.wiek = 53

obozowicz1.czy_jest_pelnoletni() #NIE
obozowicz2.czy_jest_pelnoletni() #NIE
obozowicz3.czy_jest_pelnoletni() #TAK

obozowicz3.zmien_wiek(15)

obozowicz3.czy_jest_pelnoletni() #NIE