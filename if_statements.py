# Internship Task - if, if-else, if-elif-else, nested if-else

print("IF")
for i in range(1, 4):
    if i > 0:
        print(i, "is positive")

print("\nIF-ELSE")
for i in range(-1, 2):
    if i >= 0:
        print(i, "is non-negative")
    else:
        print(i, "is negative")

print("\nIF-ELIF-ELSE")
for i in range(1, 5):
    if i == 1:
        print(i, "one")
    elif i == 2:
        print(i, "two")
    elif i == 3:
        print(i, "three")
    else:
        print(i, "other")

print("\nNESTED IF-ELSE")
for i in range(1, 6):
    if i % 2 == 0:
        if i % 4 == 0:
            print(i, "even and divisible by 4")
        else:
            print(i, "even but not divisible by 4")
    else:
        print(i, "odd")
