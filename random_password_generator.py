import random
import string

print("=" * 45)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure at least one character from each category
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Combine all characters
        all_characters = lowercase + uppercase + digits + symbols

        # Fill remaining password length
        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        # Shuffle the password
        random.shuffle(password)

        # Convert list to string
        final_password = "".join(password)

        print("\nGenerated Password:")
        print(final_password)

        choice = input("\nGenerate another password? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Random Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")