import pytest
from blizzard import Blizzard
from Storm import Storm

class Test_blizzard_classification:
    def test_severe_blizzard(self):
        blizzard = Blizzard("Blizzard 1", 50, -15)
        assert blizzard.calculate_classification() == "Severe Blizzard"

    def test_severe_blizzard_consistency(self):
        blizzard = Blizzard("Blizzard 1", 50, -15)  # Severe Blizzard conditions
        assert blizzard.calculate_classification() == "Severe Blizzard", "Error: Classification naming issue detected!"