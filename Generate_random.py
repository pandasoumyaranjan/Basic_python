import random

a = []
n = int(input("Enter Number of elements In random : "))
for item in range(n):
    a.append(random.randint(1, 100))

print('Randomised list is :')
print(a)
