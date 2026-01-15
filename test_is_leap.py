from main import is_leap

def test_is_leap_happy():
    assert is_leap(2024) == True
    assert is_leap(1980) == True
    assert is_leap(1600) == True

def test_is_leap_unhappy():
    assert is_leap(1500) == False
    assert is_leap(2006) == False
    assert is_leap(1473) == False