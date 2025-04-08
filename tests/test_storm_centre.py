import pytest
from storm_centre import StormCentre
from tornado import Tornado
from blizzard import Blizzard
from Storm import Storm
from hurricane import Hurricane

class Test_storm_centre:
    def test_add_more_than_20_storms(self):
        centre = StormCentre()

        for i in range(20):
            storm = Tornado(f"Tornado{i}", 100)
            result = centre.add_storm(storm)
            assert result == True

        # adding storm 21 to fail
        extra_storm = Tornado("Tornado21", 100)
        result = centre.add_storm(extra_storm)
        assert result == False

    def test_remove_storm_returns_true_when_removed(self):
        centre = StormCentre()
        storm = Tornado("Test remove Storm 1", 90)
        centre.add_storm(storm)

        result = centre.remove_storm("Test remove Storm 1")

        assert result == True
        assert len(centre.storm_list) == 0

    def test_add_storm_hurricane_class_instance(self):
        centre = StormCentre()
        hurricane = Hurricane("Cyclone", 120)
        result_hurricane = centre.add_storm(hurricane)

        assert result_hurricane == True
        assert centre.storm_list[0].name == "Cyclone"


"""Testing to see if will pass different type of storms"""
class FakeStorm:
    def __init__(self, name, wind_speed):
        self.name = name
        self.wind_speed = wind_speed

def test_add_storm_invalid_type():
    centre = StormCentre()
    fake = FakeStorm("Fake Storm", 123)

    result = centre.add_storm(fake)
    assert result == False