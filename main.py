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
