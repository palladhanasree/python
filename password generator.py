import random
import string

def generate_password(length):
    if length < 4:  # Ensure a minimum length for a strong password
        print("Password length should be at least 4 characters.")
        return ""
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one character from each pool
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from all pools combined
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

# Set the desired password length
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print("Generated password:", password)
