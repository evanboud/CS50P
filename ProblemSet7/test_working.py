import pytest
from working import convert

def test_validate():
    with pytest.raises(ValueError):
        convert("jfk to rkf")
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
    assert convert("9:30 PM to 9:45 AM") == "21:30 to 09:45"