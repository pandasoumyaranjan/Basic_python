num = int(input("Enter number of elements : "))

a = []
b = []

for i in range(0,num):
    a = int(input("Enter element to list A:"))
    a.append(i)

print(a)