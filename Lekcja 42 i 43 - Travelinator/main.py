klucz_API = "a5cd3ed92408ae65a82a4b9e8623c14f"

import requests
from pprint import pprint

# =========================================================================

def check_coordinates(city, klucz_API):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={klucz_API}")
    # print(response.status_code)
    # pprint(response.json())

    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    city = response.json()[0]['name']
    country = response.json()[0]['country']

    return lat, lon, city, country


def get_weather_info(lat, lon, klucz_API):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={klucz_API}&lang=PL&units=metric")

    response = response.json()

    weather = response['weather'][0]['description']
    temp = response['main']['temp']
    feels_like = response['main']['feels_like']
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']

    return weather, temp, feels_like, pressure, humidity

# ===============================================================================
# NOWE FUNCKJE POBIERANIA Z API
# ===============================================================================

def get_country_info(country_code):
    response = requests.get(f"https://countries.dev/alpha/{country_code}")
    response = response.json()

    country_name = response['name']
    capital = response['capital']

    return country_name, capital


def get_user_location():
    response = requests.get(f"https://api.country.is/")
    response = response.json()

    ip = response['ip']
    country = response['country']

    return ip, country

# ==============================================================================
# FUNKCJE WYŚWIETLAJĄCE
# ==============================================================================

def print_location_info(city):
    lat, lon, city, country_code = check_coordinates(city, klucz_API)
    country_name, capital = get_country_info(country_code)

    print(f"\Miasto: {city}")
    print(f"Kraj: {country_name}")
    print(f"Stolica kraju: {capital}")
    print(f"Współrzędne: {lat}, {lon}")


def print_weather_info(city):
    lat, lon, city, country_code = check_coordinates(city, klucz_API)
    weather, temp, feels_like, pressure, humidity = get_weather_info(lat, lon , klucz_API)

    print(f"\nPogoda w mieście {city}:")
    print(f"Warunki pogodowe: {weather}")
    print(f"Temperatura: {temp}°C")
    print(f"Temperatura odczuwalna: {feels_like}°C")
    print(f"Wilgotność: {humidity}%")
    print(f"Ciśnienie atmosferyczne: {pressure} hPa")


def print_user_location(start_city):
    ip, user_country = get_user_location()
    country_name, _ = get_country_info(user_country)

    print(f"\nTwój publiczny adres IP: {ip}")
    print(f"Kraj przypisany do adresu IP: {country_name} ({user_country})")

    if start_city is None:
        print("Nie podano jeszcze miasta startowego.")
    else:
        _, _, _, start_country = check_coordinates(start_city, klucz_API)

        if user_country == start_country:
            print("Znajdujesz się w kraju, z którego rozpoczynasz podróż.")
        else:
            print("Znajdujesz się w innym kraju niż miejsce rozpoczęcia podróży.")



# ==============================================================================
# GŁÓWNA CZĘŚĆ PROGRAMU
# ==============================================================================

print("Witaj, jetsme Travelinator, twój inteligentny asystent")

start_city = None
dest_city = None

while True:
    print("""
Jaką akcję chesz wykonać?
1. Podaj lub zmień miejsce startowe
2. Podaj lub zmień miejsce docelowe
3. Sprawdź informacje o miejscu startowym
4. Sprawdź informacje o miejscu docelowym
5. Sprawdź pogodę w miejscu startowym
6. Sprawdź pogode w meijscu docelowym
7. Sprawdź swoją lokalizację na podstawie IP
8. Zakończ program
""")
    chosen_option = input("Wybierz opcję: ")

    match chosen_option:
        case "1":
            start_city = input("Podaj nazwę miasta, z którego podróżujesz: ")

        case "2":
            dest_city = input("Podaj nazwę miasta, do którego podróżujesz: ")

        case "3":
            if start_city is not None:
                print_location_info(start_city)
            else:
                print("Najpierw podaj miasto startowe.")

            
        case "4":
            if dest_city is not None:
                print_location_info(dest_city)
            else:
                print("Najpierw podaj miasto docelowe.")
            
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            print("Do zobaczenia!")
            break
        case _:
            print("Podano błędną ocpję.")

    input("\n Naciśnij enter, aby kontynuować...")
        
            
            