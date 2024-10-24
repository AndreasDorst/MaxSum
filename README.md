# MaxSum

MaxSum is a Python console application that allows users to input integer numbers and find the number (or numbers) with the maximum sum of digits. The program continues to accept input until a zero is entered. It also includes options to limit the number of inputs and a feature that prompts the user to continue or exit after results are displayed.

## Features
- Input any number of integers and find the one with the maximum sum of digits.
- Support for an optional input limit via command-line arguments.
- Handles multiple numbers with the same maximum sum of digits.
- Prompts the user to continue or exit after displaying the result.
- Includes command-line argument parsing with `argparse` for flexibility.
  
## Prerequisites

To run this application, ensure you have Python installed on your machine. This project uses Python 3.6 or later.

- [Python 3.x](https://www.python.org/downloads/)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AndreasDorst/MaxSum.git
   cd MaxSum
   ```

2. **Create a virtual environment** (recommended but optional):

   ```bash
   python -m venv venv
   ```

   Then, activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:

   This project doesn't have external dependencies, but if you want to track dependencies, you can create a `requirements.txt` for future use.

   To generate it:
   ```bash
   pip freeze > requirements.txt
   ```

   To install dependencies (if any are added in the future):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the script directly from the command line.

1. **Run the application**:
   
   ```bash
   python max_sum_digits.py
   ```

2. **Command-line arguments**:

   - **Limit the number of inputs**:
   
     You can specify a maximum number of integers to input using the `-m` or `--max` argument:

     ```bash
     python max_sum_digits.py --max 5
     ```

## How to Use

1. **Enter integer values**:
   The application will ask you to input integer numbers. Enter numbers one by one. Type `0` to stop input.
   
2. **See results**:
   After entering the numbers, the program will display the number(s) with the maximum sum of digits.

3. **Choose to continue or exit**:
   After displaying the result, the program will ask if you'd like to continue or exit. Type `yes` to restart or `no` to exit.

## Example

```bash
$ python max_sum_digits.py
Enter an integer (0 to stop): 123
Enter an integer (0 to stop): 456
Enter an integer (0 to stop): 789
Enter an integer (0 to stop): 0

The number(s) with the maximum sum of digits (24) is/are: 789
Would you like to continue? (yes/no): no
```

## Tests

The MaxSum application includes a suite of automated tests to ensure the correctness of its functionality. The tests are written using the `unittest` framework, which is part of the Python standard library.

### Running the Tests

To run the test suite, follow these steps:

1. **Ensure you are in the project directory** where the `test_max_sum_digits.py` file is located.

2. **Execute the following command** in your terminal:

   ```bash
   python -m unittest test_max_sum_digits.py
   ```

   This command will discover and run all the tests defined in the `test_max_sum_digits.py` file.

### Test Structure

The tests cover various aspects of the application, including:

- **Sum of Digits Calculation**: Validating that the `sum_of_digits` function correctly computes the sum of digits for both positive and negative integers, as well as zero.

- **Input Handling**: Testing the `get_numbers` function to ensure it correctly collects user input, including handling invalid inputs, managing the maximum number of inputs, and determining the maximum sum of digits.

- **Multiple Inputs and Ties**: Checking scenarios where multiple numbers have the same maximum sum of digits to ensure they are all reported correctly.

Running the test suite helps ensure that the MaxSum application behaves as expected. It is recommended to run the tests after making any changes to the codebase to catch potential regressions or bugs.
