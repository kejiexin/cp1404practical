import random

print(random.randint(5, 20))  # line 1
# On line 1, I saw a random integer between 5 and 20, inclusive.
# The smallest number I could have seen was 5, the largest was 20.
print(random.randrange(3, 10, 2))  # line 2
# On line 2, I saw a random odd integer between 3 and 9, inclusive.
# The smallest number I could have seen was 3, the largest was 9.
# Line 2 could not have produced a 4, because it only generates odd numbers.
print(random.uniform(2.5, 5.5))  # line 3
# On line 3, I saw a random floating-point number between 2.5 and 5.5, inclusive.
# The smallest number I could have seen was 2.5, the largest was 5.5.
# To produce a random number between 1 and 100 inclusive, I can use the randint function again:
print(random.randint(1, 100))