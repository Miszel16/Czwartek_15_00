import json
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv



with open('menu.json', 'r', encoding='utf-8') as file:
    menu = json.load(file)

pizzas_full_info = menu['menu']

# print(pizzas_full_info)

list_of_pizzas_name = []

for p in pizzas_full_info:
    list_of_pizzas_name.append(p['pizza'])

# print(list_of_pizzas_name)


order = []
# ===============================================================================


def send_email(message_text):
    dotenv.load_dotenv()

    subject = "Pizzeria u Vita - potwierdzenie zamowienia"

    sender_email = os.getenv('sender_email')
    sender_password = os.getenv("sender_password")
    recipient_email = os.getenv("recipient_email")

    message = MIMEMultipart()

    message['Subject'] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    body_part = MIMEText(message_text)

    message.attach(body_part)

    with smtplib.SMTP("smtp.wp.pl", 587, timeout=20) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

# ===============================================================================

def display_menu():
    for index, pizza in enumerate(pizzas_full_info):
        print(f"{index + 1}")
        print(f"Pizza {pizza['pizza']}")
        print(f"Składniki: {', '.join(pizza['dodatki'])}")
        print(f"Ceny:"
              f"Mała: {pizza['ceny']['S']}zł"
              f"Średnia: {pizza['ceny']['M']}zł"
              f"Duża: {pizza['ceny']["L"]}zł"
              )
        print(" ")

    input("Wciśnij enter, aby wrócić do ekranu głównego.")

# ===============================================================================

def add_to_order():
    print("Którą pizzę chcesz zamówić: ")

    for index, pizza in enumerate(list_of_pizzas_name):
        print(f"{index + 1}. {pizza}")

    pizza_number = int(input("Podaj numer pizzy: "))
    pizza_amount = int(input("Ile pizz chcesz zamówić: "))
    size = input("Jaki rozmiar pizzy (S/M/L): ").upper()

    pizza_name = list_of_pizzas_name[pizza_number - 1]

    order.append(
        {
        'size' : size,
        'pizza_amount': pizza_amount,
        'pizza_name': pizza_name
        }
    )

    print(f"Dodano do zamówienia: {pizza_amount} x {pizza_name} [{size}]")
    time.sleep(2)


# ===============================================================================

def calculate_cost(order):
    for pizza in pizzas_full_info:
        if pizza['pizza'] == order['pizza_name']:
            cost = order['pizza_amount'] * int(pizza['ceny'][order['size']])

    return cost


# ===============================================================================

def display_order():
    print("\nTwoje zamówienie: ")

    total_cost = 0

    for pizza in order:
        cost = calculate_cost(pizza)

        print(f"{pizza['pizza_amount']} x {pizza['pizza_name']} [{pizza['size']}] : {cost}zł")
        total_cost += cost

    print(f"Łaczny koszt: {total_cost}zł")
    input("Wciśnij enter, aby wrócić do ekrnau głównego.")


# ===============================================================================

def send_order():
    text = "Dziękujemy za złożenie zamówienia:\n"
    total_cost = 0
    
    for pizza in order:
        cost = calculate_cost(pizza)
    
        print(f"{pizza['pizza_amount']} x {pizza['pizza_name']} [{pizza['size']}] : {cost}zł")
        total_cost += cost


    text += f"Łączny koszt {total_cost}zł"

    send_email(text)

    print("Zamówienie zostało złożone.")
    input("Wciśnij enter, aby kontynuować.")


# ===============================================================================

def main_page():
    while True:
        print()
        print("Witaj na stronie pizzerii u Vita!")
        print("1. Wyświetl menu")
        print("2. Dodaj pizze do zamówienia")
        print("3. Podejrzyj zamówienie")
        print("4. Wyczyść zamówienie")
        print("5. Wyślij zamówienie")
        print("6. Zakończ")

        option = input("Wybierz co chcesz zrobić: ")

        if option == "1":
            display_menu()

        elif option == "2":
            add_to_order()

        elif option == "3":
            display_order()

        elif option == "4":
            order.clear()
            print("Zamówienie wyczyszczone.")

        elif option == "5":
            send_order()

        elif option == "6":
            break

        else:
            print("Proszę wpisać poprawny numer opcji :)")


main_page()