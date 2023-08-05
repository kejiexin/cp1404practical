"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_months = int(input("How many months? "))

    for month in range(1, numbers_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes)
def print_report(incomes):


    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate (incomes, 1):

        total += income
        print(f"month{month:5} income${income:5.2f} total${total:9.2f} ")


main()