MAXIMUM_LENGTH = 10

password = input("Enter a password: ")

while len(password) < MAXIMUM_LENGTH:
    print("Invalid password. The password should be at least 10 characters long.")
    password = input("Enter a password: ")

for i in range(len(password)):
    print("*", end="")
