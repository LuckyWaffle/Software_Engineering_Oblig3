# [x] 804 -> true
# [x] 600 -> false
# [x] 400 -> true
from oblig2 import isLeapYear


def test_divisible_by_4_is_leap():
    result = isLeapYear(804)
    assert result == True


def test_divisible_by_100_is_not_leap():
    result = isLeapYear(600)
    assert result == False


def test_divisible_by_400_is_leap():
    result = isLeapYear(400)
    assert result == True