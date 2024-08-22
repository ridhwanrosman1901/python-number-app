# Python Number App

## Overview

The Python Number App is a simple command-line application that performs four key operations on user-provided numbers and strings. It allows you to:

1. **Check if a number is even or odd.**
2. **Generate a multiplication table for a number.**
3. **Identify the largest number among three inputs.**
4. **Count the number of vowels in a given string.**

## Features

### 1. Even or Odd Number Check
The app checks whether a number entered by the user is even or odd.

### 2. Multiplication Table Generator
The app generates a multiplication table for the number entered by the user.

### 3. Largest Number Checker
The app compares three numbers entered by the user and identifies the largest one.

### 4. Vowel Counter
The app counts all the vowels in a user-provided string.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ridhwanrosman1901/python-number-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-number-app
   ```

## Usage

To run the app, simply execute the `main.py` file:

```bash
python main.py
```

Follow the on-screen prompts to input numbers and strings. The app will provide the results based on your inputs.

## Preview

Here's a preview of the app in action:

![Preview](/preview1.png)

## Code

The application is implemented in Python and the code is available in the `main.py` file:

```python
# 1. Checks whether the number is even or odd.
number = int(input("Enter a number: "))
print(number)
if number % 2 == 0:
        print("The number is even.")
else:
    print("The number is odd.")

# 2. Generate a multiplication table for the number
print(f"Multiplication table for {number}:\n")
for multiplyby in range(1, 11):
    equal = number * multiplyby
    print(f"{number} x {multiplyby} = {equal}")

# 3. Checking the largest number
numberOne = int(input("Enter a number: "))
numberTwo = int(input("Enter a number: "))
numberThree = int(input("Enter a number: "))

if numberOne >= numberTwo and numberOne >= numberThree:
    largest = numberOne
elif numberTwo >= numberOne and numberTwo >= numberThree:
    largest = numberTwo
else:
    largest = numberThree

print(f"The largest number is: {largest}")

# 4. Count all vowels from a string
input_string = input("Enter any word: ")

vowel_count = 0

input_string = input_string.lower()

vowels = "aeiou"

for char in input_string:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels in the string is: {vowel_count}")
```

## Repository

[Python Number App Repository](https://github.com/ridhwanrosman1901/python-number-app.git)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```