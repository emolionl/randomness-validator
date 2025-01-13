import pytest
from randomness_validator.validator import RandomnessValidator
from datetime import datetime

# Shared variables for testing
bit_stream = [0, 1, 0, 1, 1, 0]  # Example bit stream
timestamps = [datetime.now() for _ in bit_stream]  # Mock timestamps for each bit

def test_chi_square():
    rv = RandomnessValidator()
    result = rv.chi_square_test(bit_stream)
    assert result >= 0  # Chi-square values are non-negative

def test_entropy():
    rv = RandomnessValidator()
    result = rv.entropy(bit_stream)
    assert 0 <= result <= 1  # Entropy should be within [0, 1]

def test_autocorrelation():
    rv = RandomnessValidator()
    result = rv.autocorrelation_test(bit_stream)
    assert -0.1 <= result <= 0.1  # Expected autocorrelation range

def test_monte_carlo_simulation():
    rv = RandomnessValidator()
    result = rv.monte_carlo_simulation(bit_stream, bins=2)
    assert result >= 0  # Chi-square values are non-negative

def test_check_unique():
    rv = RandomnessValidator()
    result = rv.check_unique(bit_stream)
    assert result is False  # Not all bits are unique

def test_run_all_tests():
    rv = RandomnessValidator()
    results, warnings = rv.run_all_tests(bit_stream)
    
    assert "Chi-Square Test" in results
    assert "Entropy" in results
    assert "Autocorrelation" in results
    assert "Monte Carlo Simulation" in results
    assert "Uniqueness Check" in results
    
    for test, warning in warnings.items():
        assert warning  # Ensure warnings are meaningful

def test_timestamp_handling():
    # Example test to validate timestamp association
    rv = RandomnessValidator()
    for bit, timestamp in zip(bit_stream, timestamps):
        assert isinstance(bit, int)  # Validate bits are integers
        assert isinstance(timestamp, datetime)  # Validate timestamps are datetime objects
