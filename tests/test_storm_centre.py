import pytest
from storm_centre import StormCentre
from tornado import Tornado
from hurricane import Hurricane



@pytest.mark.parametrize("num_storms, expected_result", [
    (20, True),
    (21, False)
])

def test_add_more_than_20_storms(storm_centre, storm_instance, num_storms, expected_result):
    """to test if storm_centre allows only up to 20 storms"""
    for i in range(num_storms - 1):
        storm = storm_instance(Tornado, f"Tornado{i}", 100)
        assert storm_centre.add_storm(storm) is True

    extra_storm = storm_instance(Tornado, "Tornado20", 100)
    assert storm_centre.add_storm(extra_storm) is expected_result

def test_remove_storm_returns_true_when_removed(storm_centre, storm_instance):
    """to test if removing a storm returns True and removes it from the storm list or not"""
    storm = storm_instance(Tornado, "Test remove Storm", 90)
    storm_centre.add_storm(storm)

    assert storm_centre.remove_storm("Test remove Storm") is True
    assert len(storm_centre.storm_list) == 0

def test_add_storm_hurricane_class_instance(storm_centre, storm_instance):
    """to test stor_centre successfully adds a Hurricane instance"""
    hurricane = storm_instance(Hurricane, "Cyclone", 120)
    assert storm_centre.add_storm(hurricane) is True
    assert storm_centre.storm_list[0].name == "Cyclone"

class FakeStorm:
    """fake storm class to test invalid storms"""
    def __init__(self, name, wind_speed):
        self.name = name
        self.wind_speed = wind_speed

def test_add_storm_invalid_type(storm_centre):
    """test to see if storm_centre will reject invalid storm"""
    fake_storm = FakeStorm("Fake Storm", 123)
    assert storm_centre.add_storm(fake_storm) is False
