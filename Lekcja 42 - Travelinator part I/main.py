klucz_API = "a5cd3ed92408ae65a82a4b9e8623c14f"

import requests
from pprint import pprint


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


print("Witaj, jestem Travelinator, twój inteligentny asystent")

start_city = input("Podaj nazwę miasta, z którego podróżujesz: ")
dest_city = input("Podaj nazwę miasta, do którego podróżujesz: ")

dest_lat, dest_lon, dest_city, dest_country = check_coordinates(dest_city, klucz_API)

weather, temp, feels_like, pressure, humidity = get_weather_info(dest_lat, dest_lon, klucz_API)

print(f"Wspólrzędne miasta docelowego:\n{dest_lat},\n{dest_lon},\n{dest_country}")

print(f"\nPogoda w mieście {dest_city}:")
print(f"Warunki pogodowe: {weather}")
print(f"Temperatura: {temp}°C")
print(f"Temperatura odczuwalna: {feels_like}°C")
print(f"Wilgotność: {humidity}%")
print(f"Ciśnienie atmosferyczne: {pressure} hPa")

# PRACA DOMOWA

# Rozbuduj program Travelinator o drugie API:
# https://api.country.is/
# Zapoznaj się z dokumentacją API i sprawdź, w jaki sposób pobrać:
# - publiczny adres IP użytkownika,
# - kod kraju przypisany do tego adresu.

# Utwórz funkcję get_user_location(),
# która pobierze te dane i je zwróci.
# Następnie wyświetl je w programie oraz 
# porównaj kod kraju z kodem kraju miasta początkowego.