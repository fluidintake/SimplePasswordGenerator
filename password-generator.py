# Import modules
import secrets

# Define available password characters
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_'

# Ask the user for password length
length = input("How long will your password be? ")

# Validate user input
while not length.isdigit():
    length = input("Please enter a number: ")

# Generate password
password = ""
for i in range(int(length)):
    password += secrets.choice(symbols)

# Display password
print(password)
