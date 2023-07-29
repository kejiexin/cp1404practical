"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

# Initialize a variable 'is_finished' to False to control the loop
is_finished = False

# Use a while loop to repeatedly prompt the user until a valid integer is entered
while not is_finished:
    try:
        # Attempt to get user input as an integer and store it in the 'result' variable
        result = int(input("Enter a valid integer: "))

        # If no exception is raised (input is valid integer), set 'is_finished' to True to exit the loop
        is_finished = True

        # TODO: this line
        # Add your code here to process the valid integer if needed

    # Catch the ValueError exception, which occurs when the input cannot be converted to an integer
    except ValueError:
        # If the input is not a valid integer, print an error message
        print("Please enter a valid integer.")

# Print the final valid result (entered integer) after the loop
print("Valid result is:", result)

