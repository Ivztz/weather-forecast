import pytest

from project import choice_is_valid, date_is_valid, get_range, process_regions


def test_date_is_valid():
    assert date_is_valid("2023-07-08") == True
    with pytest.raises(SystemExit):
        date_is_valid("foo")
        date_is_valid("07-08-2023")
        date_is_valid("23-07-08")
        date_is_valid("2023-7-08")
        date_is_valid("2023-07-8")


def test_get_range():
    assert get_range({'low': 60, 'high': 90}) == "60 - 90"


def test_choice_is_valid():
    assert choice_is_valid("1", 3) == True
    assert choice_is_valid("foo", 3) == False
    assert choice_is_valid("0", 4) == False
    assert choice_is_valid("4", 4) == True


def test_process_regions():
    data = {'west': 'Cloudy', 
            'east': 'Thundery Showers', 
            'central': 'Cloudy', 
            'south': 'Cloudy', 
            'north': 'Thundery Showers'}
    output = "West: Cloudy\nEast: Thundery Showers\nCentral: Cloudy\nSouth: Cloudy\nNorth: Thundery Showers"
    assert process_regions(data) == output