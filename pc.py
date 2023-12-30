"""
Project 2: Password Checker Program
Objective: Build a program that checks the strength 
of a password against a predefined set of rules. 
The program should provide feedback to the user on 
whether their password is considered strong.

"""
min_characters = 7
special_chars = ["!", "?", "#", "@", "$", "*"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function to check password strength


def check_password_strength(password):
    # Checking the length of the password
    if len(password) >= min_characters:
        HAS_7_CHARS = True
    else:
        HAS_7_CHARS = False

    # Checking for special characters
    HAS_SPECIAL_CHARS = any(char in special_chars for char in password)

    # Checking for numbers
    HAS_NUMBERS = any(char.isdigit() for char in password)

    # Provide feedback
    if HAS_7_CHARS and HAS_SPECIAL_CHARS and HAS_NUMBERS:
        print("Your password is strong.")
    else:
        if not HAS_7_CHARS:
            print("Your password should be at least 7 characters long.")
        if not HAS_SPECIAL_CHARS:
            print(
                "Your password should include at least one special character (!, ?, #, @, $, *).")
        if not HAS_NUMBERS:
            print("Your password should include at least one number.")


# State password requirements
print("\nWelcome to the password checker!\n")
print("A strong password must meet the following criteria:")
print("- At least 7 characters long\n- Include at least 1 special character\n- Include at least 1 number\n")

# Users password
users_password = input("Enter your password: ")

# Check the password strength
check_password_strength(users_password)

# Retry option
while True:
    retry = input(
        "\nWould you like to try another password? (yes/no): ").lower()
    if retry == "yes":
        users_password = input("Enter your password: ")
        check_password_strength(users_password)
    elif retry == "no":
        print("Thank you for using the password checker!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
