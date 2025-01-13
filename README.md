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
```

## Usage

```Python
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
```
## Methods
***chi_square_test(bit_stream)***
- **Args: bit_stream (list) – A list of 0s and 1s.**
- **Returns: The Chi-Square statistic (float).**
- **Description: This test measures how uniformly distributed the bitstream is by comparing observed frequencies to expected frequencies (0s and 1s).**

***entropy(bit_stream)***
- ***Args: bit_stream (list) – A list of 0s and 1s.***
- ***Returns: The entropy value (float), where values close to 1 indicate high randomness.***
- ***Description: This method computes the Shannon entropy of the bitstream. Higher values (close to 1) indicate more randomness, while values closer to 0 indicate less randomness.***

***autocorrelation_test(bit_stream)***
- ***Args: bit_stream (list) – A list of 0s and 1s.***
- ***Returns: The autocorrelation value (float), with 0 indicating no correlation.***
- ***Description: Measures how much a sequence of bits correlates with itself at a given lag. For randomness, we expect no correlation.***

***monte_carlo_simulation(bit_stream, bins=10)***
- ***Args: bit_stream (list) – A list of numbers.***
- ***bins (int) – The number of bins for histogram analysis (default: 10).***
- ***Returns: The chi-square statistic from the Monte Carlo simulation (float).***
- ***Description: This method tests the uniformity of the bitstream using a Monte Carlo simulation. It checks how evenly distributed the numbers are by dividing them into bins.***

***check_unique(bit_stream)***
- ***Args: bit_stream (list) – A list of numbers.***
- ***Returns: True if all elements are unique, False otherwise.***
- ***Description: This method checks whether all elements in the sequence are unique.***

***run_all_tests(bit_stream)***
- ***Args: bit_stream (list) – A list of numbers or bits to validate.***
- ***Returns: results (dict) – A dictionary with the test names as keys and their results as values.***
- ***warnings (dict) – A dictionary with test names as keys and warning messages for out-of-range values.***
- ***Description: Runs all the above tests and compares the results with predefined thresholds. It returns the test results and any warnings for values that are out of the acceptable range.***


## Thresholds
The ***RandomnessValidator*** uses predefined thresholds for each test:

- ***Chi-Square Test: (0, 3.84)*** – A 95% confidence interval for 1 degree of freedom.
- ***Entropy: (0.9, 1.0)*** – Entropy values close to 1 indicate good randomness.
- ***Monte Carlo Simulation: (0, 3.84)*** – Based on the chi-square for uniform distribution.
- ***Autocorrelation: (-0.1, 0.1)*** – Correlation values close to 0 are expected.
- ***Uniqueness Check: True*** – This indicates all elements in the bitstream should be unique.

## Example Usage
Here's a full example that runs the tests and displays the results:

```python
from randomness_validator import RandomnessValidator

# Initialize the validator
validator = RandomnessValidator()

# Example bitstream
bit_stream = [0, 1, 0, 1, 1, 0, 1, 0]

# Run all tests
results, warnings = validator.run_all_tests(bit_stream)

# Print the results
print("Validation Results:")
for test, result in results.items():
    print(f"{test}: {result}")

print("\nWarnings:")
for test, warning in warnings.items():
    print(f"{test}: {warning}")


```

## Contributing

We welcome contributions! If you'd like to help improve the project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License – see the LICENSE file for details.
