import base64

string = input("Enter String : ")
string_b = string.encode("utf-8")
string_c = base64.b64encode(string_b)
print(string_c)
print(string_c.decode('utf-8'))

decoded = base64.decodebytes(string_c)
print(decoded.dcode())





"""encode = base64.b64encode(string.encode('UTF-8'))
decode = base64.b64decode(string)

print(encode)
print(decode)"""