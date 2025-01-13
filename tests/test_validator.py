import pytest
import os
import json
from randomness_validator.validator import RandomnessValidator
from datetime import datetime

"""
Test file for validating randomness tests.

To run the tests with detailed output, use the following command:

    pytest -v .\tests\test_validator.py

This will show you whether each individual test passed or failed. 
Use the `-v` flag to enable verbose output, which is helpful for debugging.

Each test is labeled with PASSED or FAILED.
"""

def load_trng_data_from_files(directory):
    """
    Check if there are TRNG data files in the given directory and load them.
    If no files exist, return a mock bit stream with timestamps.

    Args:
        directory (str): The directory path where the TRNG files are stored.

    Returns:
        list: A list of tuples, each containing the bit stream (list of 0s and 1s) 
              and timestamps (list of datetime objects) for each file.
    """
    file_data = []

    # Check if the directory exists and contains files
    if os.path.exists(directory) and os.listdir(directory):
        # If there are files, load all of them
        for filename in os.listdir(directory):
            # Process only .json files
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    bit_stream = []
                    timestamps = []
                    for entry in data:
                        bit_stream.append(entry['trng_output'])
                        # Replace 'Z' with '+00:00' for proper timezone parsing
                        timestamps.append(datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00')))
                    file_data.append((bit_stream, timestamps, filename))
        print(f"Loaded data from {len(file_data)} JSON files.")
    else:
        # If no files exist, use a mock bit stream and timestamps
        print("No files found, using mock data.")
        bit_stream = [0, 1, 0, 1, 1, 0]  # Example bit stream
        timestamps = [datetime.now() for _ in bit_stream]  # Mock timestamps
        file_data.append((bit_stream, timestamps, "mock_file.json"))
        
    return file_data


# Load the TRNG data or use mock data if no files are found
directory = "tests/tests_files"  # Update with your actual directory path
file_data = load_trng_data_from_files(directory)

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_chi_square(bit_stream, timestamps, filename):
    """
    Test to validate randomness using the chi-square test.
    """
    rv = RandomnessValidator()
    result = rv.chi_square_test(bit_stream)
    print(f"Chi-Square test result for {filename}: {result}")
    # Chi-square values are expected to be non-negative
    assert result >= 0

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_entropy(bit_stream, timestamps, filename):
    """
    Test to validate randomness using entropy calculation.
    The result should be within the range of [0, 1].
    """
    rv = RandomnessValidator()
    result = rv.entropy(bit_stream)
    print(f"Entropy test result for {filename}: {result}")
    # Entropy should be within [0, 1]
    assert 0 <= result <= 1

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_autocorrelation(bit_stream, timestamps, filename):
    """
    Test to validate randomness using autocorrelation.
    The expected autocorrelation range is between -0.1 and 0.1.
    """
    rv = RandomnessValidator()
    result = rv.autocorrelation_test(bit_stream)
    print(f"Autocorrelation test result for {filename}: {result}")
    # Autocorrelation values are expected to be within the range [-0.1, 0.1]
    assert -0.1 <= result <= 0.1

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_monte_carlo_simulation(bit_stream, timestamps, filename):
    """
    Test to validate randomness using a Monte Carlo simulation.
    The result is expected to be a non-negative value.
    """
    rv = RandomnessValidator()
    result = rv.monte_carlo_simulation(bit_stream, bins=2)
    print(f"Monte Carlo simulation result for {filename}: {result}")
    # Monte Carlo results are expected to be non-negative
    assert result >= 0

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_check_unique(bit_stream, timestamps, filename):
    """
    Test to check for uniqueness of the bits.
    Since the stream has multiple bits, it should not be all unique.
    """
    rv = RandomnessValidator()
    result = rv.check_unique(bit_stream)
    print(f"Check unique test result for {filename}: {result}")
    # The result should be False as the bit stream is not entirely unique
    assert result is False

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_run_all_tests(bit_stream, timestamps, filename):
    """
    Run all the randomness tests to validate the results.
    Ensure that all necessary tests are included in the results.
    """
    rv = RandomnessValidator()
    results, warnings = rv.run_all_tests(bit_stream)
    
    # Ensure all tests are included in the results
    print(f"Results for {filename}: {results}")
    assert "Chi-Square Test" in results
    assert "Entropy" in results
    assert "Autocorrelation" in results
    assert "Monte Carlo Simulation" in results
    assert "Uniqueness Check" in results
    
    # Check that all warnings are meaningful
    for test, warning in warnings.items():
        assert warning  # Ensure warnings are meaningful

@pytest.mark.parametrize("bit_stream, timestamps, filename", file_data)
def test_timestamp_handling(bit_stream, timestamps, filename):
    """
    Test to validate that timestamps are correctly associated with each bit.
    Ensure that each bit has a corresponding timestamp.
    """
    rv = RandomnessValidator()
    for bit, timestamp in zip(bit_stream, timestamps):
        # Validate that each bit is an integer
        assert isinstance(bit, int)
        # Validate that each timestamp is a datetime object
        assert isinstance(timestamp, datetime)
    print(f"Timestamp handling test passed for {filename}")
