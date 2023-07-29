"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# A ValueError will occur when the user inputs a non-integer value for either the numerator or denominator.
# A ZeroDivisionError will occur when the user inputs 0 as the denominator.
# Yes, you can change the code to avoid the possibility of a ZeroDivisionError by adding an if statement to check if the denominator is 0 before performing the operation. Here’s an example:


try:
    # Try to get user input for the numerator and convert it to an integer
    numerator = int(input("Enter the numerator: "))

    # Try to get user input for the denominator and convert it to an integer
    denominator = int(input("Enter the denominator: "))

    # Keep asking for the denominator until a valid value (non-zero) is entered
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    # Perform the division and calculate the fraction
    fraction = numerator / denominator

    # Print the result of the division (the fraction)
    print(fraction)

# Catch the ValueError exception if the user enters non-integer values
except ValueError:
    print("Numerator and denominator must be valid numbers!")

# This block will be executed regardless of whether an exception occurred or not
# It simply prints "Finished." to indicate the end of the program
print("Finished.")
