# Function to extract name from email
def extract_name_from_email(email):
    return email.split('@')[0].title()

# Main function
def main():
    user_emails = {}  # Dictionary to store email-name pairs

    # Get email input from the user
    email = input("Email: ").strip()

    # Loop until an empty email is provided
    while email:
        name = extract_name_from_email(email)  # Extract name from email
        print(f"Is your name {name}? (Y/n)")
        response = input().strip().lower()

        if response == "n":
            name = input("Name: ").strip().title()  # Ask for name if response is 'n'

        user_emails[email] = name  # Store email-name pair in dictionary
        email = input("Email: ").strip()  # Get the next email

    # Print the collected emails and names
    print("\nEmails and Names:")
    for email, name in user_emails.items():
        print(f"{name} ({email})")

# Call the main function to start the program
main()





