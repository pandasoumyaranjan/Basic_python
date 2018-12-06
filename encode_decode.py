import base64

print("*********************MESSEGE ENCODER*********************\n")

while 1:
    print("___Select any operation.___")
    print("1.Press 1 to Encode a String : ")
    print("2.Press 2 to Decode a String : ")
    print("3.Press 3 to Exit Portal     : ")

    choice = input("Enter choice(1/2/3):")

    if choice == '1':
        str1 = input("Enter a String : ")
        encode = base64.b64encode(str1.encode('UTF-8', errors='Strict'))
        print("Encoded String Is : ", encode)

    elif choice == '2':
        str2 = input("Enter a string to Decode : ")
        decode = base64.b64decode(str2)
        print("Decoded String is Decode : ", decode)

    elif choice == '3':
        exit("\n\nExiting!!!!!!\n\n")
    else:
        print("\n\nInvalid input!!!!!\n\n")
