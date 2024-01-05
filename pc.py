"""
Project 2: Password Checker Program
Objective: Build a program that checks the strength
of a password against a predefined set of rules.
The program should provide feedback to the user on
whether their password is considered strong.

"""
# Introduction
print("Welcome to the Password Checker!")
print("\nA strong password must meet the following criteria:")
print("- It must be at least 7 characters long.")
print("- It must include at least 1 special character.")
print("- It must include at least 1 number.")
print("- It must include at least 1 uppercase letter.")
print("- It must include at least 1 lowercase letter.")

# Function to check password strength


def check_password_strength(password):
    # Check Length
    has_min_length = len(password) >= 7
    # Check for Special Characters
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "£"]
    has_special_char = any(char in special_characters for char in password)
    # Check for uppercase and lowercase
    has_uppercass = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    # Check for Numbers
    has_number = any(char.isdigit() for char in password)
    # Check for very strong password
    is_very_strong = (
        len(password) >= 10
        and sum(char in special_characters for char in password) >= 2
        and sum(char.isdigit() for char in password) >= 2
        and sum(char.isupper() for char in password) >= 2
        and sum(char.islower() for char in password) >= 2
    )

    # Providing Feedback
    if has_min_length and has_special_char and has_number and has_uppercass and has_lowercase:
        if is_very_strong:
            print("Congratulations! Your password is VERY VERY strong")
        else:
            print("Congratulations! Your password is strong.")
        return True
    else:
        print("\nYour password does not meet the following password requirements:")
        if not has_min_length:
            print("- Password should be at least 7 characters long.")
        if not has_special_char:
            print("- Password should include at least 1 special character.")
        if not has_number:
            print("- Password should include at least 1 number.")
        if not has_uppercass:
            print("- Password should include at least 1 uppercase letter.")
        if not has_lowercase:
            print("- Password should include at least 1 lowercase letter.")
        return False

# Function for the user to enter a password with retry limit


def enter_password_with_retry(max_attempts):
    attempts = 0
    while attempts < max_attempts:
        users_password = input("\nEnter a password: ")
        if check_password_strength(users_password):
            return True  # Password is strong, exit the function
        else:
            attempts += 1
            print(
                f"\nAttempts remaining: {max_attempts - attempts}")
    return False  # Maximum attempts reached


# Retry option with a limit
max_attempts = 3  # Maximum number of attempts

# User attempts to enter passwords until they decide to stop
while True:
    if enter_password_with_retry(max_attempts):
        while True:
            try_again = input(
                "\nWould you like to check another password? (yes/no): ").lower()
            if try_again == "yes":
                break  # Break from the inner loop and allow the user to enter another password
            elif try_again == "no":
                print("\nThank you for using the Password Checker!")
                exit()  # Exit the program if the user chooses not to enter another password
            else:
                print("Oops! Please enter either 'yes' or 'no'.")
    else:
        while True:
            try_again = input(
                "\nMaximum attempts reached. Would you like to try another password? (yes/no): ").lower()
            if try_again == "yes":
                break  # Break from the inner loop and allow the user to enter another password
            elif try_again == "no":
                print("\nExiting the Password Checker. Have a good day!")
                exit()  # Exit the program if the user chooses not to enter another password
            else:
                print("Oops! Please enter either 'yes' or 'no'.")
