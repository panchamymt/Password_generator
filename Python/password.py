import random

def generate_password(length):
    # Define a list of possible characters to use in the password
    characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?")
    # Shuffle the list of characters randomly
    random.shuffle(characters)
    # Select a random subset of the characters with the desired length
    password = "".join(random.sample(characters, length))
    return password

# Prompt the user to enter a desired password length
length = int(input("Enter password length: "))

# Generate a random password with the desired length
password = generate_password(length)

# Display the generated password on the screen
print("Your password is:", password)