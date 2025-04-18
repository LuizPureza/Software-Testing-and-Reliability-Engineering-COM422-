import pytest
from hurricane import Hurricane
from blizzard import Blizzard
from storm_centre import StormCentre
from tornado import Tornado


@pytest.fixture
def hurricane_instance():
    """to create Hurricane"""
    def _create_hurricane(name, wind_speed):
        return Hurricane(name, wind_speed)
    return _create_hurricane


@pytest.fixture
def blizzard_instance():
    """to create Blizzard"""
    def _create_blizzard(name, wind_speed, temperature):
        return Blizzard(name, wind_speed, temperature)
    return _create_blizzard


@pytest.fixture
def tornado_instance():
    """to create Tornado"""
    def _create_tornado(name, wind_speed):
        return Tornado(name, wind_speed)
    return _create_tornado

@pytest.fixture
def storm_centre():
    """to create a storm cetre  for each test"""
    return StormCentre()

@pytest.fixture
def storm_instance():
    """to create storm objects"""
    def _create_storm(storm_type, name, wind_speed):
        return storm_type(name, wind_speed)
    return _create_storm