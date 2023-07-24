for i in range(1, 21, 2):
    print(i, end=' ')
print()




for i in range(0, 110, 10):

    print(i, end=' ')

print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part c: Print n stars
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end="")
print()

# Part d: Print n lines of increasing stars
for i in range(1, n+1):
    print("*" * i)
