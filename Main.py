# import regex library
import re
# import systym module
import sys
# import os
import os

## user modules
# import utilities module
import Utilities
# import usersOP module
import UsersOP
# import users class
from UsersOP import Users
# import Encryption for secuirty of passwords and sensitive data
import Encrypt

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
        print("#####################################################")
        print("##############     Login From        ################")
        print("#####################################################")
        # take user email
        logged_user = None
        while True:
            login_email = Utilities.get_input("Enter Your Email","email",re)
            if UsersOP.get_data_by_key(file_path_index,file_path_data,login_email) is not None:
                login_password_db = UsersOP.get_data_by_key(file_path_index, file_path_data, login_email)["Password"]
                break
            else:
                print("No Users With This Email!!")
        # Take user password 
        login_password = Utilities.get_input("Enter Your Password","default",re)
        # Simulate a login attempt
        if not Encrypt.validate_password(login_password, login_password_db):
            print("Incorrect password. Access denied.")
        else:
            print("### Login Success ###")
            logged_user = Users(UsersOP.get_data_by_key(file_path_index, file_path_data, login_email))
        
            # start Menu after login
            print("Welcome " + logged_user.First_name)

    ## register option
    if menu1_input == 2:
        print("#####################################################")
        print("##############     Register From     ################")
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
                ##print("unique")
                break
            else:
                print("This Email Already Used, Where U Here Before !!")
        # taking user password
        while True:
            register_password = Utilities.get_input("Enter Your Password","password",re)
            confirm_register_password = Utilities.get_input("Enter Your Password Again","default",re)
            if register_password == confirm_register_password:
                print("password confirmation correct")
                # Create a SHA-256 hash object
                stored_hashed_password = Encrypt.hash_password(register_password)
                break
            else:
                print("Error Passwords Does Not Match !!! , Enter it again")
        # take user phone number
        register_phone = Utilities.get_input("Enter Your Phone Number","phone",re)
        # create the user
        register_user_data = {"First_name":register_first_name,"Last_name":register_last_name,"Email":register_email,"Password":stored_hashed_password,"Phone":register_phone}
        register_user = Users(register_user_data)
        register_user.register(file_path_data,file_path_index)
        # clean object for memory and security 
        del register_user
        os.system('clear')
        print("##############  Registration Succeeded ################")

    ## exit option
    if menu1_input == 3:
        print("########### Best ##### OF ###### LUCK ###############")
        print("##############       FUNDPRO         ################")
        print("####### it seems impossible until it's done #########")
        print("#####################################################")
        sys.exit()
