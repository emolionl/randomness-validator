import pytest
from randomness_validator.validator import RandomnessValidator

def test_chi_square():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.chi_square_test()
    assert result >= 0  # Chi-square values are non-negative
