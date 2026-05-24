import random
import string

def generate_password(length=12):
    if length < 3:
        return "Error: Length must be at least 3 characters."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_chars = string.punctuation
    combined_pool = lowercase + uppercase + special_chars
    
    # Ensure at least one lowercase, uppercase, and special character
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(special_chars)
    ]
    
    password += [random.choice(combined_pool) for _ in range(length - 3)]
    random.shuffle(password)
    
    return "".join(password)

if __name__ == "__main__":
    print("--- Password Generator (Letters & Special Characters) ---")
    try:
        user_input = input("Enter password length (default 12): ")
        length = int(user_input) if user_input.strip() else 12
        
        result = generate_password(length)
        print(f"Generated Password: {result}")
    except ValueError:
        print("Error: Invalid number entered.")