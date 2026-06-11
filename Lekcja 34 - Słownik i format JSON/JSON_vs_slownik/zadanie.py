import pprint
import json

gra = {"tytul" : "CS",
       "rok_wydania" : 1999,
       "wydawca" : "valve",
       "gatunek" : "strzelanka"}


with open("l1.json", "r") as file:
    spis = json.load(file)

spis["spis_gier"].append(gra)

pprint.pprint(spis["spis_gier"])


with open("l2_spis.json", "w") as file:
    json.dump(spis, file, indent = 4, sort_keys=True)

