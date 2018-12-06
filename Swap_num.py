def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    print("After Swap the Value of A:", a, "Value of B:", b)


a = int(input("Enter value for A : "))
b = int(input("Enter value for B : "))

print("Value in A is: ", a, "Value in B is: ", b)
swap(a, b)






