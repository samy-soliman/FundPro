# get user input function
# it reads user input and validates it against a specified regex
def get_input(output_message,input_type,re_module):
    # define our regex
    name_regex = r'^[A-Za-z][a-z]*$'
    email_regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    egypt_phone_regex = r'^01\d{9}$'
    default_regex =  r'^.*$'
    if input_type == "name":
        match_regex = name_regex
    elif input_type == "email":
        match_regex = email_regex
    elif input_type == "password":
        match_regex = password_regex
    elif input_type == "phone":
        match_regex = egypt_phone_regex
    elif input_type == "default":
        match_regex = default_regex
    while True:
        print(output_message)
        user_input = input()
        if re_module.match(match_regex, user_input):
            print("Correct")
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
            elif input_type == "default":
                print("Error! Wrong Input Format")