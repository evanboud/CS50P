import pytest
from numb3rs import validate

def test_validate():
    assert validate("222.222.222.222") == True
    assert validate("1.cat.1.1") == False
    assert validate("255.256.256.256") == False