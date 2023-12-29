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

passwords = ["helloworld", "imchange69",
             "ilovecookies!23", "python1@gmail.com"]

HAS_7_CHARS = False
HAS_SPECIAL_CHARS = False
HAS_NUMBERS = False

# State password requirements
print("\nWelcome to the password checker!\n")
print("A strong password must meet the following criteria:")
print("- At least 7 characters long\n- Include at least 1 special character\n- Include at least 1 number\n")

# Users password
users_password = input("Enter your password: ")

# check requirements (lenght, special characters, number)
# provide feeedback
# retry option
