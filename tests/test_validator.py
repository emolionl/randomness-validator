import pytest
from randomness_validator.validator import RandomnessValidator

def test_chi_square():
    """Test the chi-square test with a simple bitstream."""
    rv = RandomnessValidator()
    result = rv.chi_square_test([0, 1, 0, 1, 1, 0])
    assert result >= 0  # Chi-square values are non-negative

def test_entropy():
    """Test the entropy calculation with a balanced bitstream."""
    rv = RandomnessValidator()
    result = rv.entropy([0, 1, 0, 1, 1, 0])
    assert 0 <= result <= 1  # Entropy should be within [0, 1]

def test_autocorrelation():
    """Test the autocorrelation calculation with a simple bitstream."""
    rv = RandomnessValidator()
    result = rv.autocorrelation_test([0, 1, 0, 1, 1, 0])
    assert -1 <= result <= 1  # Autocorrelation should be within [-1, 1]

def test_monte_carlo():
    """Test the Monte Carlo simulation with a simple bitstream."""
    rv = RandomnessValidator()
    result = rv.monte_carlo_simulation([0, 1, 0, 1, 1, 0], bins=2)
    assert result >= 0  # Chi-square values are non-negative

def test_uniqueness():
    """Test the uniqueness check for a bitstream."""
    rv = RandomnessValidator()
    result = rv.check_unique([0, 1, 0, 1, 1, 0])
    assert not result  # The input bitstream has duplicates

def test_run_all_tests():
    """Test running all randomness tests and ensure results are within expected ranges."""
    rv = RandomnessValidator()
    results, warnings = rv.run_all_tests([0, 1, 0, 1, 1, 0])

    # Check that results are returned for all tests
    assert 'Chi-Square Test' in results
    assert 'Entropy' in results
    assert 'Autocorrelation' in results
    assert 'Monte Carlo Simulation' in results
    assert 'Uniqueness Check' in results

    # Verify that warnings are generated for out-of-range values
    for test_name, warning in warnings.items():
        assert test_name in results  # Ensure warning corresponds to a test
