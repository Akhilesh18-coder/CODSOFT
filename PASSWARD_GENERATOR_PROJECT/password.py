import random
import string

print("Welcome to the Password Generator!")

# Ask user for the password length
length = int(input("Enter the desired password length: "))

# Characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for i in range(length))

# Display the password
print("Your generated password is:", password)
