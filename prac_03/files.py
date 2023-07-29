# Define the file name
file = "name.txt"

# Open the file in write mode to write user input (name) into the file
out_file = open(file, "w")

# Ask the user to input their name
name = input("user name: ")

# Write the user's name to the file
print(name, file=out_file)

# Close the file after writing the name
out_file.close()




# Define the file name to be read
file = "name.txt"

# Open the file in read mode to read its content
in_file = open(file)

# Read the entire content of the file into the 'text' variable
text = in_file.read()

# Close the file after reading its content
in_file.close()

# Print the content of the file
print(text)



try:
    # Try to open the file "numbers.txt" in read mode using a 'with' statement
    # The 'with' statement ensures that the file is automatically closed after leaving the block
    with open("numbers.txt", "r") as file:
        # Read the first line of the file and convert it to an integer, store it in 'num1'
        num1 = int(file.readline())
        # Read the second line of the file and convert it to an integer, store it in 'num2'
        num2 = int(file.readline())
        # Print the sum of 'num1' and 'num2'
        print(num1 + num2)

# If the file "numbers.txt" is not found (raises FileNotFoundError)
except FileNotFoundError:
    # Print an error message indicating that the file was not found
    print("File not found.")

# Open the file "numbers.txt" in read mode to read its content
in_file = open("numbers.txt", "r")

# Initialize a variable 'total' to store the running sum of numbers read from the file
total = 0

# Iterate through each line in the file
for line in in_file:
    # Convert the current line to an integer (assuming it contains a number)
    number = int(line)

    # Add the number to the 'total' sum
    total += number

# Close the file after reading its content
in_file.close()

# Print the final total sum of all numbers from the file
print(total)












