# Etap 1
# - pobieranie danych
# - baza danych ze słowami
# - tłumaczeniem słów na liczby


zero = ["0", "zerem", "zero", "zerowy","zera"]
jeden = ["1", "jeden", "jednym", "jedynka", "jedynkę"]

plus = ["+", "dodać", "plus", "zsumować", 'dodac', "zsumowac"]
baza = [zero, jeden, plus]

# ----------------------------------------------------------
#   FUNCKJE
# ----------------------------------------------------------
def przetlumacz(slowo: str) -> str: # 'jeden'
    for baza_symbolu in baza: #baza_symbolu = jeden
        for slowo_bazy_symbolu in baza_symbolu: # slowo_bazy_symbolu = "jeden"
            if slowo == slowo_bazy_symbolu:
                return baza_symbolu[0]
    return ''


def oblicz_z_tekstu(dzialanie: str): # '0-9'  albo '+'
    liczba1 = ''
    liczba2 = ''
    znak = ''

    for i in dzialanie:
        if i.isdigit():
            if znak == "":
                liczba1 += i
            else:
                liczba2 += i
        else:
            znak = i
    
    if liczba1=="" or liczba2=="" or znak=="":
        return "Nie rozumiem działania - sprawdź słowa."
    
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)

    return oblicz(liczba1, liczba2, znak)


def oblicz(l1: int, l2: int, znak: str):
    # + , - , * , /
    if znak == "+":
        return l1+l2
    elif znak == "-":
        return l1-l2
    elif znak == "*":
        return l1*l2
    elif znak in ("/", ":"): # znak == "/" or znak == ":"
        if l2 == 0:
            return "Error: Nie można dzielić przez 0!"
        else:
            return l1/l2

# ----------------------------------------------------------


tekst = input("Podaj tekst: ").lower()

dzialanie = ""

for slowo in tekst.split(" "):
    slowo_przetlumaczone = przetlumacz(slowo)
    dzialanie += slowo_przetlumaczone

print(dzialanie) # '11+10'

print(oblicz_z_tekstu(dzialanie))