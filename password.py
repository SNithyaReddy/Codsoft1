import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the length is valid
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Function to prompt user input and generate password
def main():
    print("--- Password Generator ---")
    
    # User input for the length of the password
    try:
        length = int(input("Enter the desired length for the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Generate password
    password = generate_password(length)
    
    if password:
        print(f"\nGenerated Password: {password}")

# Run the program
main()
