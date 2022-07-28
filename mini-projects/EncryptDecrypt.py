def encrypt(message, shift):
    mess_enc = ""
    for c in message:
        if 'a' <= c <= 'z':
            if ord(c) + shift <= 122:
                mess_enc += chr(ord(c) + shift)
            else:
                mess_enc += chr(ord(c) + shift - 26)
        elif 'A' <= c <= 'Z':
            if ord(c) + shift <= 90:
                mess_enc += chr(ord(c) + shift)
            else:
                mess_enc += chr(ord(c) + shift - 26)
        else:
            mess_enc += c
    return mess_enc


def decrypt(message, shift):
    mess_dec = ""
    for c in message:
        if 'a' <= c <= 'z':
            if ord(c) - shift < 97:
                mess_dec += chr(ord(c) - shift + 26)
            else:
                mess_dec += chr(ord(c) - shift)
        elif 'A' <= c <= 'Z':
            if ord(c) - shift < 65:
                mess_dec += chr(ord(c) - shift + 26)
            else:
                mess_dec += chr(ord(c) - shift)
        else:
            mess_dec += c
    return mess_dec


choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message\n")
shift = int(input("Type shift number:\n"))
if choice == 'encode':
    print(f"The encoded message is {encrypt(message, shift)}")
elif choice == 'decode':
    print(f"The decoded text is {decrypt(message, shift)}")
else:
    print("You Entered Wrong Choice")


