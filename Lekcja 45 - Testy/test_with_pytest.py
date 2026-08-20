import pytest
import funkcje

# python -m pytest test_with_pytest.py -v

def test_add():
    assert funkcje.add(2,4) == 6
    assert not funkcje.add(1,1) == 4

def test_add_negatives():
    assert funkcje.add(0, -5) == -5


# --------------------------------------
def test_palindroms():
    assert funkcje.is_palindrom("kamilslimak") == True
    assert funkcje.is_palindrom("kamyk") == False