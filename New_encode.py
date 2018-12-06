import base64
string_a = input("Enter a String :")

#string_b = string_a.encode('utf-8')
#base64_bytes = base64.b64encode(string_b)
#print(base64_bytes)
str3 = string_a.decode('utf-8')
print(str3)

base64_decoded_bytes = base64.decodebytes(str3)
print(base64_decoded_bytes.decode())
