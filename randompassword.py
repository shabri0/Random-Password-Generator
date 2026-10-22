import random
import string
password_length = int(input("Enter the desired password length: "))
if password_length < 1:
    print("Password length must be at least 1.")        
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"Generated password: {password}")