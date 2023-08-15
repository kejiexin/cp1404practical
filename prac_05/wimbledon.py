import csv

# Function to read data from a CSV file
def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    return data

# Function to get champions and their win counts
def get_champions_and_counts(data):
    champions_counts = {}
    for row in data:
        champion_name = row[2]
        if champion_name in champions_counts:
            champions_counts[champion_name] += 1
        else:
            champions_counts[champion_name] = 1
    return champions_counts

# Function to get a sorted list of unique countries
def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)

# Main function to process data and display results
def main():
    filename = "wimbledon.csv"  # CSV file name
    data = read_csv_file(filename)  # Read data from CSV

    champions_counts = get_champions_and_counts(data)  # Get champions and their win counts
    countries = get_countries(data)  # Get sorted list of unique countries

    print("Wimbledon Champions:")
    for champion, count in champions_counts.items():
        print(f"{champion} {count}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_string = ", ".join(countries)
    print(countries_string)

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
