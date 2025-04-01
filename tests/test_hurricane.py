import pytest
from hurricane import Hurricane
from blizzard import Blizzard
from tornado import Tornado
from Storm import Storm
from storm_centre import StormCentre


class Test_hurricane_classification():

    def test_hurricane_classification(self):
        hurricane = Hurricane("Hurricane 1", 73)
        assert hurricane.calculate_classification() == "Tropical Storm"