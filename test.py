import pytest
from hurricane import Hurricane
from blizzard import Blizzard
from Storm import Storm
from storm_centre import storm_centre


class TestHurricane:
    def test_classification(self):
        assert Hurricane("StormA", 80).classification == "Category one"
        assert Hurricane("StormB", 130).classification == "Category four"
        assert Hurricane("StormC", 160).classification == "Category five"
        assert Hurricane("StormD", 70).classification == "Tropical Storm"

    def test_advice(self):
        assert Hurricane("StormA", 80).get_advice() == "Close storm shutters and stay away from windows"
        assert Hurricane("StormB", 130).get_advice() == "Coastal regions are encouraged to evacuate"
        assert Hurricane("StormC", 160).get_advice() == "Evacuate"


class TestBlizzard:
    def test_classification(self):
        assert Blizzard("Blizz1", 40, -5).classification == "Snow Storm"
        assert Blizzard("Blizz2", 35, -10).classification == "Blizzard"
        assert Blizzard("Blizz3", 50, -15).classification == "Severe Blizzard"

    def test_advice(self):
        assert Blizzard("Blizz1", 40, -5).get_advice() == "Take care and avoid travel if possible."
        assert Blizzard("Blizz2", 35, -10).get_advice() == "Keep warm, Do not travel unless absolutely essential."
        assert Blizzard("Blizz3", 50, -15).get_advice() == "Keep warm, avoid all travel."


class TestStormCentre:
    def setup_method(self):
        self.centre = StormCentre()

    def test_add_storm(self):
        storm1 = Hurricane("StormX", 100)
        assert self.centre.add_storm(storm1) is True
        assert len(self.centre.storms) == 1

    def test_duplicate_storm(self):
        storm1 = Hurricane("StormX", 100)
        storm2 = Hurricane("StormX", 120)
        self.centre.add_storm(storm1)
        assert self.centre.add_storm(storm2) is False

    def test_remove_storm(self):
        storm = Hurricane("StormY", 110)
        self.centre.add_storm(storm)
        assert self.centre.remove_storm("StormY") is True
        assert self.centre.remove_storm("StormZ") is False

    def test_update_storm(self):
        storm = Hurricane("StormZ", 90)
        self.centre.add_storm(storm)
        assert self.centre.update_storm("StormZ", {"wind_speed": 130}) is True
        assert storm.wind_speed == 130


class TestStorm:
    def test_storm_initialization(self):
        class TestStormClass(Storm):
            def __init__(self, name, wind_speed):
                super().__init__(name, wind_speed)
                self.classification = "Test"

        storm = TestStormClass("StormTest", 50)
        assert storm.name == "StormTest"
        assert storm.wind_speed == 50
