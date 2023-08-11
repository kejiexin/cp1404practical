# Main function to count word frequencies and display results
def main():
    word_count = {}  # Dictionary to store word frequencies
    user_input = input("Enter a string: ")  # Get user input
    words = user_input.split()  # Split the input into words using spaces

    # Count the frequency of each word in the input
    for word in words:
        frequency = word_count.get(word, 0)  # Get the current frequency or default to 0
        word_count[word] = frequency + 1  # Increment the frequency by 1

    max_key_length = max(len(key) for key in word_count.keys())  # Find the length of the longest word for formatting

    sorted_items = sorted(word_count.items())  # Sort the word-frequency pairs

    # Print the sorted word-frequency pairs with aligned formatting
    for key, value in sorted_items:
        print(f"{key:{max_key_length}} : {value}")  # Format output with aligned columns

# Call the main function to run the program
main()





