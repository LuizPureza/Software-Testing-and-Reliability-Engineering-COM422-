import pytest
from hurricane import Hurricane


@pytest.mark.parametrize("name, wind_speed, expected_category", [
    ("Hurricane Cat5", 160, "Category five"),
    ("Hurricane Cat4", 140, "Category four"),
    ("Hurricane Cat3", 120, "Category three"),
    ("Hurricane Cat2", 100, "Category two"),
    ("Hurricane Cat1", 80, "Category one"),
    ("Tropical Storm", 60, "Tropical Storm"),
])

def test_hurricane_classification(hurricane_instance, name, wind_speed, expected_category):
    """to test multiple hurricane classifications"""
    hurricane = hurricane_instance(name, wind_speed)
    assert hurricane.calculate_classification() == expected_category

@pytest.mark.parametrize("name, wind_speed, expected_category", [
    ("Hurricane Test 1", 74, "Category one"),
    ("Hurricane Test 2", 73, "Tropical Storm"),
])
def test_hurricane_tropical_storm(hurricane_instance, name, wind_speed, expected_category):
    """to test difference between Hurricane and Tropical Storm"""
    hurricane = hurricane_instance(name, wind_speed)
    assert hurricane.calculate_classification() == expected_category