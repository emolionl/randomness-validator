import math
from collections import Counter
import numpy as np

class RandomnessValidator:
    """
    A class to validate the randomness of a sequence of numbers or bits.
    Methods include chi-square, entropy, autocorrelation, Monte Carlo simulation,
    and uniqueness checks. Thresholds are customizable for each test.

    Attributes:
        thresholds (dict): Predefined thresholds for randomness tests.
    """

    def __init__(self):
        """
        Initializes the RandomnessValidator with predefined thresholds.
        """
        self.thresholds = {
            'Chi-Square Test': (0, 3.84),  # 95% confidence interval for 1 degree of freedom
            'Entropy': (0.9, 1.0),  # Entropy close to 1 indicates good randomness
            'Monte Carlo Simulation': (0, 3.84),  # Based on chi-square for uniform distribution
            'Autocorrelation': (-0.1, 0.1),  # Correlation close to 0 is expected
            'Uniqueness Check': True  # True indicates all bits are unique
        }

    def chi_square_test(self, bit_stream):
        """
        Performs a chi-square test to measure the uniformity of the bitstream.

        Args:
            bit_stream (list): A list of 0s and 1s.

        Returns:
            float: The chi-square statistic.
        """
        expected_frequency = len(bit_stream) / 2
        observed_frequency = [bit_stream.count(0), bit_stream.count(1)]
        chi_square = sum((observed - expected_frequency) ** 2 / expected_frequency for observed in observed_frequency)
        return chi_square

    def entropy(self, bit_stream):
        """
        Calculates the Shannon entropy of the bitstream.

        Args:
            bit_stream (list): A list of 0s and 1s.

        Returns:
            float: The entropy value, where values close to 1 indicate high randomness.
        """
        counts = Counter(bit_stream)
        total = len(bit_stream)
        return -sum(count / total * math.log2(count / total) for count in counts.values())

    def autocorrelation_test(self, bit_stream):
        """
        Measures autocorrelation in the bitstream.

        Args:
            bit_stream (list): A list of 0s and 1s.

        Returns:
            float: The autocorrelation value, with 0 indicating no correlation.
        """
        lag = 1  # Using lag 1 for simplicity
        autocorrelation = sum(bit_stream[i] == bit_stream[i + lag] for i in range(len(bit_stream) - lag))
        return autocorrelation / len(bit_stream)

    def monte_carlo_simulation(self, bit_stream, bins=10):
        """
        Conducts a Monte Carlo simulation to test uniformity.

        Args:
            bit_stream (list): A list of numbers.
            bins (int): The number of bins for histogram analysis.

        Returns:
            float: The chi-square statistic from the simulation.
        """
        hist, _ = np.histogram(bit_stream, bins=np.arange(0, bins + 1))
        expected_frequency = len(bit_stream) / bins
        chi_square = sum((obs - expected_frequency) ** 2 / expected_frequency for obs in hist)
        return chi_square

    def check_unique(self, bit_stream):
        """
        Checks if all elements in the bitstream are unique.

        Args:
            bit_stream (list): A list of numbers.

        Returns:
            bool: True if all elements are unique, False otherwise.
        """
        unique_bits = set(bit_stream)
        return len(unique_bits) == len(bit_stream)

    def run_all_tests(self, bit_stream):
        """
        Executes all randomness tests and checks results against predefined thresholds.

        Args:
            bit_stream (list): A list of numbers or bits to validate.

        Returns:
            tuple: A dictionary of test results and a dictionary of warnings for out-of-range values.
        """
        results = {
            'Chi-Square Test': self.chi_square_test(bit_stream),
            'Entropy': self.entropy(bit_stream),
            'Autocorrelation': self.autocorrelation_test(bit_stream),
            'Monte Carlo Simulation': self.monte_carlo_simulation(bit_stream),
            'Uniqueness Check': self.check_unique(bit_stream)
        }

        warnings = {}
        for test, result in results.items():
            if test in self.thresholds:
                threshold = self.thresholds[test]
                if isinstance(threshold, tuple):  # Numeric range
                    if not (threshold[0] <= result <= threshold[1]):
                        warnings[test] = f"Out of range: {result} (Expected {threshold[0]}-{threshold[1]})"
                elif isinstance(threshold, bool):  # Boolean check
                    if result != threshold:
                        warnings[test] = f"Out of range: {result} (Expected {threshold})"
        return results, warnings

# Example Usage
if __name__ == "__main__":
    validator = RandomnessValidator()
    bit_stream = [0, 1, 0, 1, 1, 0, 1, 0]
    results, warnings = validator.run_all_tests(bit_stream)
    print("Validation Results:", results)
    print("Warnings:", warnings)
