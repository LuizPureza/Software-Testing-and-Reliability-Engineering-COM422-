import pytest
from tornado import Tornado



@pytest.mark.parametrize("name, wind_speed, expected_wind_speed", [
    ("Test Tornado", 150, 150),
])

def test_invalid_initialization(tornado_instance, name, wind_speed, expected_wind_speed):
    """to test tornado validating wind speed."""
    tornado = tornado_instance(name, wind_speed)
    assert tornado.wind_speed == expected_wind_speed

@pytest.mark.parametrize("name, wind_speed, expected_classification", [
    ("Test Tornado 2", 40, "F0"),
])

def test_classification_unclassified(tornado_instance, name, wind_speed, expected_classification):
    """to test tornado classification thinking"""
    tornado = tornado_instance(name, wind_speed)
    assert tornado.calculate_classification() == expected_classification

@pytest.mark.parametrize("name, wind_speed, expected_advice", [
    ("Tornado Unclassified test 1", 230, "Find underground shelter, crouch near to the floor covering your head with your hands"),
    ("Tornado Unclassified test 2", 30, "There is no need to panic"),
])

def test_tornado_advice(tornado_instance, name, wind_speed, expected_advice):
    """to test tornado advice using various wind speeds."""
    tornado = tornado_instance(name, wind_speed)
    assert tornado.get_advice() == expected_advice