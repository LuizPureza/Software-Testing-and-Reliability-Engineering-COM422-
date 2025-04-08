import pytest
from tornado import Tornado

class Test_tornado_init_parameters:
    def test_invalid_initialization(self):
        tornado = Tornado("Test Tornado", 150)
        assert tornado.wind_speed == 150

    def test_classification_unclassified(self):
        tornado = Tornado("Test Tornado 2", 40)  # 40 should be classified as "F0"
        assert tornado.calculate_classification() == "F0"



"""Get Advice testing"""


class Test_tornado_advice:
    def test_unclassified_advice_1(self):
        tornado = Tornado("Tornado Unclassified test 1", 230)
        assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"

    def test_unclassified_advice_2(self):
        tornado = Tornado("Tornado Unclassified test 2", 30)
        advice = tornado.get_advice()
        assert advice == "There is no need to panic"
