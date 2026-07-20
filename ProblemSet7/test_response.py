import pytest
from response import validating


def test_validating():
    with pytest.raises(AssertionError):
        validating("malan@@@harvard.edu")
    assert validating("evanboud@gmail.com") == "Valid"
   

