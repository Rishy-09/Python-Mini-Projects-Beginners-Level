import random
import string

# this asks for minimum length and it will go beyond it if the conditions of numbers, special_characters has not been satisfied till then
def generate_password(min_length, numbers=True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False


    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

# checking for every digit if it is the additional character that user has permitted to add and so it is , then further checking if it has been added and length has been filled
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        # if numbers should be added and number has appeared then updating the meets_criteria to true 
        if numbers:
            meets_criteria = has_number
        # and so goes for special_characters so atleast 1 number of 1 special_character be appeared in password if user allows
        if special_characters:
            meets_criteria = meets_criteria and has_special


    return pwd


min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you eant to have special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)

'''
This case explains the use of words and conditions that are applied here:
Enter the minimum length: 1
Do you want to have numbers (y/n)? y
Do you eant to have special characters (y/n)? y
The generated password is: Anf'q(4 
'''