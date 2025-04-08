import pytest
from blizzard import Blizzard
from Storm import Storm

class Test_blizzard_classification:

    def test_severe_blizzard_classification(self):
        blizzard = Blizzard("Blizzard test 1", 50, -12)
        assert blizzard.calculate_classification() == "Severe Blizzard"

    def test_blizzard_classification(self):
        blizzard = Blizzard("Blizzard test 2",40, -5)
        assert blizzard.calculate_classification() == "Blizzard"

    def test_snow_storm_classification(self):
        blizzard = Blizzard("Blizzard test 3", 34, -5)
        assert blizzard.calculate_classification() == "Snow Storm"

class Test_blizzard_get_advice:

    def test_severe_blizzard_advice(self):
        blizzard = Blizzard("Blizzard test 4", 50, -15)
        assert blizzard.get_advice() == "Keep warm, avoid all travel."

    def test_blizzard_advice_lowercase_b(self):
        blizzard = Blizzard("Blizzard test 5", 40, -5)
        assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."
