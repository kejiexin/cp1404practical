import random

# Function to determine the score status based on the provided score
def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # Ask the user for their score
    user_score = float(input("Enter your score: "))
    user_score_status = determine_score_status(user_score)
    print("Your score status:", user_score_status)

    # Generate a random score
    random_score = random.randint(0, 100)
    random_score_status = determine_score_status(random_score)
    print("Random score:", random_score)
    print("Random score status:", random_score_status)

if __name__ == "__main__":
    main()
