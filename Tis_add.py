strin = input("Enter your string : ")
word = strin.split()
pat = input("Enter to add word :")
new_list = [x + pat for x in word]
final = "" .join(new_list)
print(final)


