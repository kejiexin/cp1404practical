"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


input_score = float(input("Enter score: "))
score_status = calculate_score(input_score)
print(score_status)
