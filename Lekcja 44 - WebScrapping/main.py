import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from io import BytesIO


# ctrl+shift + P
# Python: Select Interpreter 
# .venv

URL = "https://pokemondb.net/pokedex/game/lets-go-pikachu-eevee"

#Ćwiczenie 
def scrap_pokemon_names():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(response)
    # print(soup)

    cards = soup.find_all("div", class_="infocard")

    for card in cards:
        name = card.find("a", class_="ent-name")
        print(name.get_text())


# scrap_pokemon_names()
#---------------------------------------------------------------------

# PROJEKT - POKEDEX
# nazwa, id, typy, adres obrazka

def scrap_pokemon_list():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    pokemons_list = []

    cards = soup.find_all("div", class_="infocard")

    for card in cards:
        name = card.find("a", class_="ent-name").get_text()
        number = card.find("small").get_text()

        types = []
        for pokemon_type in card.find_all("a", class_="itype"):
            types.append(pokemon_type.get_text())

        image_url = card.find("img")["src"]

        pokemon = (
            name,
            number,
            types,
            image_url
        )

        pokemons_list.append(pokemon)

    return pokemons_list



def get_pokemon_image(image_url):
    response = requests.get(image_url)

    return response.content


def safe_name(name):
    name = name.replace("♀", "F")
    name = name.replace("♂", "M")

    return name


def add_pokemon_page(pdf, pokemon, image):
    name = pokemon[0]
    name = safe_name(name)
    number = pokemon[1]
    types = pokemon[2]

    pdf.add_page()

    # Nagłówek
    pdf.set_fill_color(220, 50, 60) # RGB 
    pdf.rect(0, 0, 148, 32, "F")

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 18)

    pdf.set_xy(10, 10)
    pdf.cell(128, 10, f"{number} {name}", align="C")

    # Tło
    pdf.set_fill_color(245,245,245)
    pdf.rect(10, 40, 128, 140, "F")

    # Obrazek
    pdf.image(BytesIO(image), x=34, y=48, w=80)

    # TYPE
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("Helvetica", "B", 13)

    pdf.set_xy(10, 140)
    pdf.cell(128, 10, "TYPE", align="C")

    # typ pokemona
    pdf.set_font("Helvetica", size=12)

    pdf.set_xy(10, 153)
    pdf.cell(128, 10, " / ".join(types).upper(), align="C")


# GŁÓWNY PROGRAM

pokemons = scrap_pokemon_list()

pdf = FPDF(format="A5")
pdf.set_auto_page_break(False)


for pokemon in pokemons:
    image = get_pokemon_image(pokemon[3])
    add_pokemon_page(pdf, pokemon, image)
    print(pokemon[1], pokemon[0], "- gotowe")

pdf.output("pokedex.pdf")
print("Gotowe! Utoworzono pdf.")
    
