# import Encryption for secuirty of passwords and sensitive data
import Encrypt

# import os
from os import system 

## user modules
# import utilities module
from Utilities import get_input

# import users class from Users.py
from Users import Users

def login_form(file_path_index,file_path_data):
    print("#####################################################")
    print("##############     Login From        ################")
    print("#####################################################")
    # take user email
    logged_user = None
    while True:
        login_email = get_input("Enter Your Email","email")
        if Users.get_user_data(file_path_index,file_path_data,login_email) is not None:
            login_password_db = Users.get_user_data(file_path_index, file_path_data, login_email)["Password"]
            break
        else:
            print("No Users With This Email!!")
    # Take user password 
    login_password = get_input("Enter Your Password","default")
    # Simulate a login attempt
    if not Encrypt.validate_password(login_password, login_password_db):
        print("Incorrect password. Access denied.")
    else:
        print("### Login Success ###")
        logged_user = Users(Users.get_user_data(file_path_index, file_path_data, login_email))
    
        # start Menu after login
        print("Welcome " + logged_user.First_name)


def register_form(file_path_index,file_path_data):
    print("#####################################################")
    print("##############     Register From     ################")
    print("#####################################################")
    # start taking user input one by one
    # taking user First Name
    register_first_name = get_input("Enter Your First Name","name")
    # taking user Last Name
    register_last_name = get_input("Enter Your Last Name","name")
    # taking user email
    while True:
        register_email = get_input("Enter Your Email","email")
        if Users.get_user_data(file_path_index,file_path_data,register_email) is None:
            ##print("unique")
            break
        else:
            print("This Email Already Used, Where U Here Before !!")
    # taking user password
    while True:
        register_password = get_input("Enter Your Password","password")
        confirm_register_password = get_input("Enter Your Password Again","default")
        if register_password == confirm_register_password:
            print("password confirmation correct")
            # Create a SHA-256 hash object
            stored_hashed_password = Encrypt.hash_password(register_password)
            break
        else:
            print("Error Passwords Does Not Match !!! , Enter it again")
    # take user phone number
    register_phone = get_input("Enter Your Phone Number","phone")
    # create the user
    register_user_data = {"First_name":register_first_name,"Last_name":register_last_name,"Email":register_email,"Password":stored_hashed_password,"Phone":register_phone}
    register_user = Users(register_user_data)
    register_user.register(file_path_data,file_path_index)
    # clean object for memory and security 
    del register_user
    system('clear')
    print("##############  Registration Succeeded ################")