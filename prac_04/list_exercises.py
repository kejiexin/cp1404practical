numbers = []

# Input five numbers and add them to the 'numbers' list
for num in range(5):
    user = int(input("Enter the number: "))
    numbers.append(user)

# Print the first number in the list
print("The first number is", numbers[0])

# Print the last number in the list
print("The last number is", numbers[-1])

# Print the smallest number in the list using the min() function
print("The smallest number is", min(numbers))

# Print the largest number in the list using the max() function
print("The largest number is", max(numbers))

# Calculate and print the average of the numbers in the list
print("The average of the numbers is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Prompt the user for a username
user = input("Enter the name: ")

# Check if the entered username is in the list of usernames
if user in usernames:  # Use 'in' to check membership in the list
    print("Access granted")
else:
    print("Access Denied")



