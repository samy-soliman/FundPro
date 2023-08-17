# import regex library
import re
# import os
import os
# user modules #
# import utilities module
import Utilities
# welcome message
print("#####################################################")
print("welcome to fundpro website, where dreams becomes true")
print("#####################################################")
print("##############       FUNDPRO         ################")
print("#####################################################")

# Start Program main menu (menu1) register or login
# start a loop until a valid input is taken or exit
while True:
    print("Enter Your Option Number: ")
    print("1) Login")
    print("2) Register")
    print("3) Exit")
    menu1_input = input()
    if re.match("^[1-3]{1}$", menu1_input):
        os.system('clear')
        break
    else:
        print("Wrong Input format, Please Enter a valid input")

menu1_input=int(menu1_input)
## login option
if menu1_input == 1:
    pass
## register option
if menu1_input == 2:
    print("#####################################################")
    print("##############     Login From        ################")
    print("#####################################################")
    # start taking user input one by one
    # taking user First Name
    register_first_name = Utilities.get_input("Enter Your First Name","name",re)
    # taking user Last Name
    register_last_name = Utilities.get_input("Enter Your Last Name","name",re)
    # taking user email
    register_email = Utilities.get_input("Enter Your Email","email",re)
    # taking user password
    while True:
        register_password = Utilities.get_input("Enter Your Password","password",re)
        confirm_register_password = Utilities.get_input("Enter Your Password Again","default",re)
        if register_password == confirm_register_password:
            print("password confirmation correct")
            break
        else:
            print("Error Passwords Does Not Match !!! , Enter it again")
    # take user phone number
    register_phone = Utilities.get_input("Enter Your Phone Number","phone",re)

## exit option
if menu1_input == 3:
    print("#####################################################")
    print("##############       FUNDPRO         ################")
    print("#####################################################")