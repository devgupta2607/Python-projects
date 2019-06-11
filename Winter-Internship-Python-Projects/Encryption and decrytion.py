alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 9
message = input("Enter the message: ")
check = input("You want to encrypt or decrypt message : ")
if check == 'encrypt':
    newmessage = ""
    for i in message:
        if i in alphabet:
            position = alphabet.find(i)
            newposition= (position + key)%26
            newmessage += alphabet[newposition]
        else:
            newmessage+=i
    print("Encrypted message: ",newmessage)

elif check == 'decrypt':
    decrypt = ""

    for i in message:
        if i in alphabet:
            pos = alphabet.find(i)
            newpos = (pos-key)%26
            decrypt += alphabet[newpos]
        else:
            decrypt+=i
    print("Decrypted message: ",decrypt)

