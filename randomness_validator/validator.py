import math
from collections import Counter
import numpy as np

class RandomnessValidator:
    def __init__(self):
        self.data = []
        self.timestamps = []

    def add_numbers(self, numbers, timestamps=None):
        self.data.extend(numbers)
        if timestamps:
            self.timestamps.extend(timestamps)

    def chi_square_test(self):
        expected_frequency = len(self.data) / len(set(self.data))
        observed_frequency = Counter(self.data)
        chi_square = sum((obs - expected_frequency) ** 2 / expected_frequency for obs in observed_frequency.values())
        return chi_square

    def entropy(self):
        counts = Counter(self.data)
        total = len(self.data)
        return -sum(count / total * math.log2(count / total) for count in counts.values())

    # Add other tests here...

    def run_validation(self):
        results = {
            "Chi-Square Test": self.chi_square_test(),
            "Entropy": self.entropy(),
        }
        return results
