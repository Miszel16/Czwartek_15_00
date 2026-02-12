# https://giganciprogramowania.edu.pl/kursy/1853:wstep-do-ai-i-programowania-w-pythonie-online?kind=Kursy+z+AI+i+programowania

# https://drive.google.com/file/d/1vbeVjGeX5m9ESRhrSuxiWAFnfvgDVBqM/view?usp=sharing

# Zadania powtórzeniowe


# Zadanie 1 – FizzBuzz
# Celem zadania FizzBuz jest napisanie programu, który wypisze na ekranie liczby 1 do 100,
# - zamiast liczb podzielnych przez 3 ma napisać Fizz, (+)
# - zamiast podzielnych przez 5 Buzz, (+)
# - zamiast podzielnych przez 3 i 5 FizzBuzz.

#  start (0) - pierwsza która się pojawi
#  stop  - pierwsza ktora się nie pojawi 
#  step (1) - zawsze dodajemy 

# +, -, *, /, //, **, %(modulo)

def FizzBuzz(start: int, stop: int):
    for i in range(start, (stop+1)):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


#--------------------------------------------------------------------------------------------------------
# Zadanie 2 - wzór
# Napisz program, który wyświetli na ekranie ten wzór, zależnie od liczby jaką podamy:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

liczba = int(input("Podaj liczbę: ")) # 6

# 1 2 3 4 5 6
# start = 0, stop = liczba+1 (7), step =1
# 
for i in range(1, liczba+1): # i = 3
    for wiersz in range(i): # [0,1,2] range(0,3,1)
        print(i, end=" ")
    print()


#--------------------------------------------------------------------------------------------------------
# Zadanie 3 – min i max
# Należy napisać program, który z listy pokaże nam najmniejszą i największą liczbę

lista = [1, 3, 7, 11, 2, -6, 0]

# print(max(lista))
# print(min(lista))
mininum = lista[0]
maximum = lista[0]

for i in lista:
    if i < mininum:
        mininum = i
    if i > maximum:
        maximum = i

print(f"minimalna: {mininum}, maksymalna: {maximum}")





#--------------------------------------------------------------------------------------------------------
# Zadanie 4 – zliczanie liter
# Program ma zliczyć ile danych liter znajduje się w zdaniu
# Przykładowe wyświetlanie:
# "ABC przykladowy tekst na potrzeby naszego programu"






#--------------------------------------------------------------------------------------------------------
# Zadanie 5 – orzeł i reszka
# Gracz będzie zgadywać co wypadnie następne, i punkty będzie dostawać albo gracz, albo komputer.


