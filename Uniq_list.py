a = []
n = int(input("Enter the number of elements : "))

for i in range(0, n):
    element = int(input("Enter element " + str(i + 1) + ":"))
    a.append(element)

b = set()
unique = [0]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
        unique.sort()
print("Non Duplicate items : ", unique)
