# - tabele z wynikami dla jednego gracza
# - ilość tur = ilość kategorii punktów

# ETAP 1 

# 1. Rzucanie wybranymi kośćmi
# 2. Wyświetlić co wyrzuciliśmy
# 3. Czy rzucamy jeszcze raz?
# 4. Ponowne rzuty (2 max.)
# 5. Wyświetlenie tabeli wyników
# 6. Gdzie chcemy wpisać?
# 7. Wstawienie punktów
# 8. Pętla gry

import random

kosci = [0,0,0,0,0]
#        0 1 2 3 4

kategorie = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ['', '', '', '', '', '']


# 
def rzuc_koscmi(numery_kosci: str):
    for i in numery_kosci: 
        index = int(i) - 1
        kosci[index] = random.randint(1,6)



def sprawdz_czy_przerzucic() -> bool:
    wybor = input("Czy chcesz przerzucic któreś z kości? (t/n)").lower()
    if wybor == 't':
        return True
    else:
        return False


def pokaz_kosci():
    print("_____________")
    for i in range(len(kosci)):
        print(f'   {i+1}. {kosci[i]}')
    print("_____________")


def pokaz_tabele_punktow():
    pierwszy_wiersz = ""
    drugi_wiersz = ""
    
    for i in range(len(kategorie)):
        pierwszy_wiersz += str(i+1) + '. ' + kategorie[i] + ' | '
        drugi_wiersz += str(punkty[i]).center(len(kategorie[i]) + 3) + ' | '
    
    print("__________________________________________________________________________")
    print(pierwszy_wiersz)
    print("--------------------------------------------------------------------------")
    print(drugi_wiersz)
    print("__________________________________________________________________________")


def punkty_w_szkole(pole):
    liczba_punktow = 0
    for kosc in kosci:
        if kosc == pole:
            liczba_punktow += kosc
    punkty[pole-1] = liczba_punktow


def wstaw_punkty():
    pole = int(input("Gdzie chcesz wpisać punkty? (Podaj numer rubryki): ")) # -1
    if punkty[pole-1] == '':
        if 1 <= pole <= len(kategorie):
            punkty_w_szkole(pole)
    else:
        print("Wybrane pole jest już uzupełnione.")
        wstaw_punkty()


        
    



pokaz_tabele_punktow()
for tura in range(len(kategorie)):
    print("Pierwsza rzut w turze: ")
    rzuc_koscmi('12345')
    pokaz_kosci()

    for i in range(2):
        przerzut = sprawdz_czy_przerzucic() # True/False
        if przerzut:
            kosci_do_przerzutu = input("Które kości chcesz przerzucić? (Podaj numery bez spacji): ") # '34'
            rzuc_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break
    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()

print(f"Twój łączny wynik to: {sum(punkty)}")
