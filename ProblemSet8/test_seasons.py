import pytest
from seasons import Date_convert
from datetime import datetime
from datetime import date

def test_str():
    Date = Date_convert(Date_Of_Birth="01-02-2002", today=date(2026, 7, 19))
    assert str(Date) == "Twelve million, eight hundred sixty-four thousand, nine hundred sixty minutes"
    



  