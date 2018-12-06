def linear_search(arr,item):
    for i in range(0,len(arr)):
        if arr[i] == item:
            return i

arr = []
num = int(input("Enter number of elements : "))

for item in range (0,num):
    data = int(input("Enter item :"))
    arr.append(data)
item = 0
print(arr)
item = int(input("Enter item to search : "))
result = linear_search(arr,item)
if result != -1:
    print(item,"found at position :",result+1)
else:
    print("Element not found !")
