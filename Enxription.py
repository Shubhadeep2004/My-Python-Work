import random
import string

chars=" "+string.ascii_letters +string.digits +string.punctuation
chars=list(chars)
key=chars.copy()

random.shuffle(key)

actual_text=input("Enter themessage:")
encripted_text=""

#Encryption
for letter in actual_text:
    index=key.index(letter)
    encripted_text += chars[index]

print(f"The actual text is :{actual_text}")
print(f"The encripted text is :{encripted_text}")

#Decription
encripted_text=input("Enter the encripted text:")
plain_text=""
for letter in encripted_text:
    index=chars.index(letter)
    plain_text += key[index]


print(f"The encripted text is :{encripted_text}")
print(f"The actual text is :{plain_text}")