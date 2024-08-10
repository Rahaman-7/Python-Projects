# ENCRPYT AND DECRPYT
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = list.copy(chars)
random.shuffle(keys)
#print(f"chars: {chars}")
#print(f"keys: {keys}")

plain_text = input("Enter a Message:"  )
cipher_text = ""

# ENCRPYT
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]
print(f"The original message: {plain_text}")
print(f"The Encrpyt message:  {cipher_text}")

# DECRPYT
cipher_text = input("Enter a Message:"  )
plain_text = ""
for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]
print(f"The Original message:  {cipher_text}")
print(f"The DEcrpyt message:  {plain_text}")