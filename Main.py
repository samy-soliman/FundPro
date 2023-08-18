# import regex library
import re

# import os
import os

## user modules
# import utilities module
import Utilities
# import usersOP module
import UsersOP
# import users class
from UsersOP import Users
##################### initialization #####################
# file path of our DB

file_path_data = "FundProData.txt"
file_path_index = "FundProIndex.txt"

# Open the file in append mode, which creates the file if it doesn't exist , and do not modify if exists
if not os.path.exists(file_path_data):
    with open(file_path_data, "a") as f:
        pass
if not os.path.exists(file_path_index):
    with open(file_path_index, "a") as f:
        pass

##################### start program execute ##################
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
    while True:
        register_email = Utilities.get_input("Enter Your Email","email",re)
        if UsersOP.get_data_by_key(file_path_index,file_path_data,register_email) is None:
            print("unique")
            break
        else:
            print("This Email Already Used, Where U Here Before !!")
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
    # create the user
    register_user = Users(register_first_name,register_last_name,register_email,register_password,register_phone)
    register_user.register(file_path_data,file_path_index)

## exit option
if menu1_input == 3:
    print("#####################################################")
    print("##############       FUNDPRO         ################")
    print("#####################################################")