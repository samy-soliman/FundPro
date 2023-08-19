# import regex library
from re import match as matchregex
# import getpass for securing password
from getpass import getpass


# get user input function
# it reads user input and validates it against a specified regex
def get_input(output_message,input_type):
    # define our regex
    name_regex = r'^[A-Za-z][a-z]*$'
    email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    egypt_phone_regex = r'^01\d{9}$'
    alphabet_regex = r'[A-Za-z]+(?: [A-Za-z]+)*'
    positive_number_regex = r'^[1-9]\d*$'
    date_regex = r'^(?:(?:19|20)\d\d)-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$'
    default_regex =  r'^.*$'
    # define our used regex based on function call
    if input_type == "name":
        match_regex = name_regex
    elif input_type == "email":
        match_regex = email_regex
    elif input_type == "password":
        match_regex = password_regex
    elif input_type == "phone":
        match_regex = egypt_phone_regex
    elif input_type == "alphabet_regex":
        match_regex = alphabet_regex
    elif input_type == "positive_number_regex":
        match_regex = positive_number_regex
    elif input_type == "date_regex":
        match_regex = date_regex
    elif input_type == "default" or input_type == "default_hide":
        match_regex = default_regex
    # start executing reading user input and validating
    while True:
        print(output_message)
        if input_type == "password" or input_type == "default_hide":
            user_input = getpass()
        else:
            user_input = input()
        if matchregex(match_regex, user_input):
            ##print("Correct")
            return user_input
        else:
            if input_type == "name":
              print("Please Enter only alphabetic characters and your first character is only allowed to be capital")
            elif input_type == "email":
                print("Error!, Enter valid Email Address, example \"SamY1_Soliman-2@hostname.Com\" \"1_Soliman.Mohamed@hostname.orG\" ")
            elif input_type == "password":
                print("Error!, Enter a Minimum length of 8 characters,\nAt least one alphabetical character (uppercase and lowercase)\nAt least one digit\nAt least one special character from @$!%*#?& ")
            elif input_type == "phone":
                print("Error! Wrong Format,Your number should start with 01 follwed by 9 digits")
            elif input_type == "alphabet_regex":
                print("Error! Wrong Input Format, Enter only Alphabetic Characters")
            elif input_type == "positive_number_regex":
                print("Error! Wrong Input Format, Enter a Number Bigger Than Zero")
            elif input_type == "date_regex":
                print("Error! Wrong Date Format, example \"2023-08-18\"")
            elif input_type == "default" or input_type == "default_hide":
                print("Error! Wrong Input Format")