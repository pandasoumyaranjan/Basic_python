def binary_search(arr,left,right,item):
    if right >=1:
        mid = left + (right - 1)/2

        if arr[mid] == item:
            return mid
        if arr[mid] > item:
            binary_search(arr,left,mid-1,item)
        else:
            binary_search(arr,mid+1,right,item)

    else:
        return -1

arr = []
num = int(input("Enter number of elements : "))

for item in range (0,num):
    data = int(input("Enter item :"))
    arr.append(data)
    arr.sort()
item = 0
left = 0
right = len(arr)
print(arr)
x = int(input("Enter item to search : "))
result = binary_search(arr,left,right,x)
if result != -1:
    print(item,"found at position :",result+1)
else:
    print("Element not found !")

