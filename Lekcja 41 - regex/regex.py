import re


print("re.match()") # szuka od początku stringa 

zdanie = "Ala ma kota"
#         012345678910

wynik1 = re.match(r"ala", zdanie)
print(wynik1) # object match

wynik2 = re.match(r"kota", zdanie)
print(wynik2) # none


# print(f"Znaleziono {wynik1.group()}")
# print(f"Początek dopasowania pod indeksem: {wynik1.start()}")
# print(f"Koniec dopasowania pod indeksem: {wynik1.end()}")
# print(f"Krotka przedziału: {wynik1.span()}") 

wynik3 = re.match(r"ala", zdanie, re.IGNORECASE)
print(wynik3)


## CIEKAWOSTKA
#               ^[1-4]?.?.?.$
##

# [1-4]? - cyfry 1-4 opcjonalne
# .?  -  jeden dodwolny znak opcjonalnie
# .?  -  jeden dodwolny znak opcjonalnie
# .   -  jeden dodwolny znak


print("\n\n\nre.search()") # znajduje pierwsze dopasowanie

zdanie = "A1la ma 10 kotów i 10 psów."

wynik1 = re.search(r"\b\d+\b", zdanie)
print(wynik1) # 



print("\n\n\nre.findall()") # znajduje wszytsko

zdanie = "Ala i Maja jada na wycieczkę do Warszawy."
wynik1 = re.findall(r"\b[A-Z][a-z]+\b",zdanie)

print(wynik1)




print("\n\n\nre.sub()") # 
# re.sub(pattern, repl, string, count=0, flags=0)

# repl - na co podmienić
# count - maksymalnej liczbie zmian (0 - domyślnie wszytsko)

text = "Roblox to najlepsza gra na świecie."
print(text)
wzor = "Roblox"
nowe = "Minecraft"
new_text = re.sub(wzor, nowe, text)
print(new_text)