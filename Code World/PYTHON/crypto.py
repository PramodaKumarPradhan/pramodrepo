from cryptography.fernet import Fernet

# generating the key
theKey = Fernet.generate_key()

# variable holding the value of key
first = Fernet(theKey)

# the plain text is converted into cipher text using the encrypt() method
theToken = first.encrypt(b"Hello, I am Indian")

# printing the encrypted message
print("Encrypted Message: ", theToken)

# the cipher text is converted back into plain text using the decrpyt() method
decryptMsg = first.decrypt(theToken)

# printing the decrypted message
print("\nDecrypted Message: ", decryptMsg)

