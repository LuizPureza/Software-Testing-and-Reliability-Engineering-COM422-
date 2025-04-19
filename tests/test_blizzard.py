import pytest
from blizzard import Blizzard



@pytest.mark.parametrize("name, wind_speed, temperature, expected_classification", [
    ("Blizzard Severe Test", 45, -12, "Severe Blizzard"),
    ("Blizzard Normal Test", 40, -5, "Blizzard"),
    ("Snow Storm Test", 34, -5, "Snow Storm"),
])

def test_blizzard_classification(blizzard_instance, name, wind_speed, temperature, expected_classification):
    """tests blizzard classification in several scenarios"""
    blizzard = blizzard_instance(name, wind_speed, temperature)
    assert blizzard.calculate_classification() == expected_classification

@pytest.mark.parametrize("name, wind_speed, temperature, expected_advice", [
    ("Blizzard Severe Advice", 50, -15, "Keep warm, avoid all travel."),
    ("Blizzard Advice", 40, -5, "Keep warm, Do not travel unless absolutely essential."),
])

def test_blizzard_get_advice(blizzard_instance, name, wind_speed, temperature, expected_advice):
    """tests blizzard advice - based on classification"""
    blizzard = blizzard_instance(name, wind_speed, temperature)
    assert blizzard.get_advice() == expected_advice

