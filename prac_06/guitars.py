from guitar import Guitar


def main():
    current_year = 2022
    guitars = []
    print("My Guitar")
    name = input("name:")
    while name != "":
        name = input("name:")
        year = int(input("year:"))
        cost = float(input("cost:$"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f'{guitar} added')
        name = input("name:")

        guitars.append(("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(("Another Guitar", 2013, 2500.00))

        print("These are my guitars:")


    for i, guitar in enumerate(guitars, start=1):
        vintage_status = "vintage" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:8.2f} ({vintage_status})")

    print("Programmer Efficiency Note")
main()

