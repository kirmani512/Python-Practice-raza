import random
import string

text=input("Enter the text")

reversed=text[::-1]

# random.choices() is a function in Python's random module that helps you randomly pick elements from a population (like a list or string).

random_chars_start = ''.join(random.choices(string.ascii_letters + string.digits, k=3)) #join is a method that a list of strings

random_chars_end = ''.join(random.choices(string.ascii_letters + string.digits, k=3))


if len(text)>3:
    encrypted_text = random_chars_start + reversed + random_chars_end

    print(encrypted_text)
else:
    encrypted_text=reversed
    
    print(reversed)

if len(text)>3:
    decrypted_text=encrypted_text[len(random_chars_start):-len(random_chars_end)]

    original_text=decrypted_text[::-1]

    print(original_text)

else:
    decrypted_text=encrypted_text[::-1]
    print(decrypted_text)