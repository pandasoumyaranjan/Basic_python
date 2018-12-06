import string

str = input("Enter The Sentence : ")

string_rem = input("Enter word you want to remove : ")

word_list = str.split()
print(' '.join([i for i in word_list if i not in string_rem]))
print("\n")