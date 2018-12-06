string = input("Enter string : ")
rep = input("Enter ori_word : ")
word_list = string.split()
#print(word_list)
if word_list[0] == rep:
    print("1st word of String can't be replaced")
else:
    string=string.replace(rep , input("rep_word : "))

print("Modified string : ")
print(string)
