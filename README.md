# RandomnessValidator

`RandomnessValidator` is a Python library for validating the randomness of a sequence of numbers or bits. It includes several statistical tests such as the Chi-Square test, entropy, autocorrelation, Monte Carlo simulation, and a uniqueness check. The library provides customizable thresholds for each test to assess whether the given sequence meets the expected level of randomness.

## Features

- **Chi-Square Test**: Measures how uniformly distributed the bitstream is.
- **Entropy Calculation**: Computes the Shannon entropy of the bitstream, where values close to 1 indicate high randomness.
- **Autocorrelation Test**: Analyzes the correlation between consecutive bits.
- **Monte Carlo Simulation**: Assesses the uniformity of the bitstream through histogram analysis.
- **Uniqueness Check**: Verifies whether all elements in the sequence are unique.
- **Customizable Thresholds**: Set thresholds for each test to determine pass/fail criteria.

## Installation

To use `RandomnessValidator`, simply clone this repository or copy the code into your project.

```bash
git clone https://github.com/yourusername/randomness-validator.git

from randomness_validator import RandomnessValidator

# Create an instance of the RandomnessValidator
validator = RandomnessValidator()

# Define your bitstream
bit_stream = [0, 1, 0, 1, 1, 0, 1, 0]

# Run all tests
results, warnings = validator.run_all_tests(bit_stream)

# Display results and warnings
print("Validation Results:", results)
print("Warnings:", warnings)
