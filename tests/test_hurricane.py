import pytest
from hurricane import Hurricane



class Test_hurricane_classification:

    def test_hurricane_classification(self):
        hurricane = Hurricane("Hurricane test 1", 74)
        assert hurricane.calculate_classification() == "Category one"

    def test_tropical_storm(self):
        hurricane = Hurricane("Hurricane test 2", 73)
        assert hurricane.calculate_classification() == "Tropical Storm"

    def test_hurricane_category_order(self):
        assert Hurricane("Test Cat5", 160).calculate_classification() == "Category five"
        assert Hurricane("Test Cat4", 140).calculate_classification() == "Category four"
        assert Hurricane("Test Cat3", 120).calculate_classification() == "Category three"
        assert Hurricane("Test Cat2", 100).calculate_classification() == "Category two"
        assert Hurricane("Test Cat1", 80).calculate_classification() == "Category one"
        assert Hurricane("Test Storm", 60).calculate_classification() == "Tropical Storm"