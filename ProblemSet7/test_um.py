import pytest
from um import count

def test_count():
    assert count("um") == 1
    assert count("yummy") == 0
    assert count("Um, hum") == 1