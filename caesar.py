def encrypt(msg, key):
    cipher = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cipher += chr((ord(char) - base + key) % 26 + base)
        else:
            cipher += char
    return cipher

def decrypt(msg, key):
    return encrypt(msg, -key)


plain = input("Enter message to encrypt: ")
key_value = int(input("Enter key value: "))


encrypted_text = encrypt(plain, key_value)
decrypted_text = decrypt(encrypted_text, key_value)


print("\nEncrypted:", encrypted_text)
print("Decrypted:", decrypted_text)


with open("output.txt", "w") as file:
    file.write("Original Message: " + plain + "\n")
    file.write("Key: " + str(key_value) + "\n")
    file.write("Encrypted: " + encrypted_text + "\n")
    file.write("Decrypted: " + decrypted_text + "\n")

print("\nOutput saved to 'output.txt'")
