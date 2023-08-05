numbers = []

for num in range(5):
    user = int(input("enter the numbers"))
    numbers.append(user)
print("The first number is", numbers[0]) # print the first number
print("The last number is", numbers[-1]) # print the last number
print("The smallest number is", min(numbers)) # print the smallest number
print("The largest number is", max(numbers)) # print the largest number
print("The average of the numbers is", sum(numbers) / len(numbers)) # print the average of the numbers

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user = input("Enter the name: ")
if user == usernames:
     print("Access granted")
else:
    print("Access Denied")


