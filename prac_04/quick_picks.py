import random
picks = int(input("How many quick picks?"))
for i in range(0, picks):
    numbers = []
    you_numbers = []
    numbers_remain = 45
    for i in range(1, 46):
        numbers.append(i)

    for i in range(0, 6):
        random_numbers = random.randint(0, numbers_remain - 1)
        you_numbers.append(numbers[random_numbers])
        numbers.remove(numbers[random_numbers])
        numbers_remain = numbers_remain - 1
    print(sorted(you_numbers))


