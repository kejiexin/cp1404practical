from guitar import Guitar


current_year = 2022
first_name = "Gibson L-5 CES"
second_name = "Another Guitar"
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 2500.00)

expected_guitar1_age = 100
expected_guitar2_age = 9
expected_guitar1_vintage = True
expected_guitar2_vintage = False

guitar1_age = guitar1.get_age(current_year)
guitar2_age = guitar2.get_age(current_year)
guitar1_vintage = guitar1.is_vintage(current_year)
guitar2_vintage = guitar2.is_vintage(current_year)

print(f'{first_name} get_age() - Expected {expected_guitar1_age}. Got {guitar1_age}. {" " if expected_guitar1_age == guitar1_age else "Mismatched! "}')
print(f"{second_name}, get_Age() - Expected {expected_guitar2_age}. Got {guitar2_age}. {'Matched!' if expected_guitar2_age == guitar2_age else 'Mismatched!'}")
print(f"{first_name} is_Vintage() - Expected {expected_guitar1_vintage}. Got {guitar1_vintage}. {'Matched!' if expected_guitar1_vintage == guitar1_vintage else 'Mismatched!'}")
print(f"{second_name} is_Vintage() - Expected {expected_guitar2_vintage}. Got {guitar2_vintage}. {'Matched!' if expected_guitar2_vintage == guitar2_vintage else 'Mismatched!'}")

