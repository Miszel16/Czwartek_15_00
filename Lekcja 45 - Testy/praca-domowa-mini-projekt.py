# Zadanie — napraw kalkulator zamówienia

# Otrzymujesz funkcję calculate_order(), która ma obliczać końcową cenę zamówienia w sklepie.

# Funkcja przyjmuje:

# price — cenę jednego produktu,
# quantity — liczbę produktów,
# discount — rabat procentowy,
# delivery_cost — koszt dostawy.
# Zasady działania programu

# Funkcja powinna:

# - policzyć cenę wszystkich produktów,
# - odjąć podany rabat procentowy,
# - ustawić darmową dostawę, jeśli wartość zamówienia po rabacie wynosi co najmniej 200 zł,
# - zwrócić -1, jeśli:
#   - cena produktu jest ujemna,
#   - liczba produktów jest równa 0 lub ujemna,
#   - rabat jest mniejszy niż 0 lub większy niż 100.


# Twoje zadanie
# Poniższa funkcja zawiera kilka błędów.

# 1. Napisz testy jednostkowe sprawdzające jej działanie.
# 2. Uruchom testy i sprawdź, które przypadki nie działają.
# 3. Na podstawie wyników testów znajdź błędy w funkcji.
# 4. Popraw funkcję tak, aby wszystkie napisane przez Ciebie testy przechodziły poprawnie.
# 5. Wykonaj testy zarówno w unittest, jak i pytest.


# Funkcja do poprawienia
def calculate_order(price, quantity, discount, delivery_cost):
    total = price * quantity

    discount_value = total / discount
    total = total - discount_value

    if total > 200:
        delivery_cost = 0

    if price < 0:
        return -1

    return total + delivery_cost


# Nie poprawiaj funkcji od razu — najpierw spróbuj znaleźć problemy za pomocą testów!!!