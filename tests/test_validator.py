import pytest
from randomness_validator.validator import RandomnessValidator

def test_chi_square():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.chi_square_test()
    assert result >= 0  # Chi-square values are non-negative

# Test for Entropy
def test_entropy():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.entropy()
    assert 0 <= result <= 1, "Entropy should be between 0 and 1"

# Test for Autocorrelation
def test_autocorrelation():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.autocorrelation_test()
    assert isinstance(result, float), "Autocorrelation should return a float value"
    assert -1 <= result <= 1, "Autocorrelation should be between -1 and 1"

# Test for Monte Carlo Simulation
def test_monte_carlo():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.monte_carlo_simulation()
    assert result >= 0, "Monte Carlo Simulation result should be non-negative"

# Test for Uniqueness Check
def test_uniqueness_check():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    result = rv.check_unique()
    assert isinstance(result, bool), "Uniqueness check should return a boolean"

# Test for Adding Numbers
def test_add_numbers():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    assert len(rv.numbers) == 6, "The numbers should be added correctly to the validator"

# Test for Validation Results
def test_validation_results():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0])
    results = rv.validate()
    assert isinstance(results, dict), "Validation results should return a dictionary"
    assert "Chi-Square Test" in results, "Validation results should include Chi-Square Test"
    assert "Entropy" in results, "Validation results should include Entropy"
    assert "Autocorrelation" in results, "Validation results should include Autocorrelation"
    assert "Monte Carlo Simulation" in results, "Validation results should include Monte Carlo Simulation"
    assert "Uniqueness Check" in results, "Validation results should include Uniqueness Check"
    assert "Timestamps" in results, "Validation results should include Timestamps"
    assert "Warnings" in results, "Validation results should include Warnings"

# Test for Timestamps
def test_timestamps():
    rv = RandomnessValidator()
    rv.add_numbers([0, 1, 0, 1, 1, 0], timestamps=[100, 101, 102, 103, 104, 105])
    assert len(rv.timestamps) == 6, "Timestamps should be added correctly"
    assert rv.timestamps[0] == 100, "The first timestamp should match the input"