# import Encryption for secuirty of passwords and sensitive data
import Encrypt
# import systym module
from  sys import exit
# import os
from os import system 

## user modules
# import utilities module
from Utilities import get_input

# import users class from Users.py
from Users import Users
# import project class from projects.py
from Projects import Projects

# login user form
def login_form(index_file_path,data_file_path):
    print("#####################################################")
    print("##############     Login From        ################")
    print("#####################################################")
    # take user email
    logged_user = None
    while True:
        login_email = get_input("Enter Your Email","email")
        if Users.get_user_data(index_file_path,data_file_path,login_email) is not None:
            login_password_db = Users.get_user_data(index_file_path, data_file_path, login_email)["Password"]
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
        return Users(**Users.get_user_data(index_file_path, data_file_path, login_email))

# register user form
def register_form(index_file_path,data_file_path):
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
        if Users.get_user_data(index_file_path,data_file_path,register_email) is None:
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
    register_user = Users(register_first_name,register_last_name,register_email,stored_hashed_password,register_phone)
    register_user.register(index_file_path,data_file_path)
    # clean object for memory and security 
    del register_user
    system('clear')
    print("##############  Registration Succeeded ################")

# exit option function in main menu
def exit_main_form():
    print("########### Best ##### OF ###### LUCK ###############")
    print("##############       FUNDPRO         ################")
    print("####### it seems impossible until it's done #########")
    print("#####################################################")
    exit()

# create project form
def create_project_form(index_file_path,data_file_path,logged_user):
    print("##############     Project From     ################")
    # start taking user input one by one
    # taking project title
    project_title = get_input("Enter Your Project Title","name")
    # taking project details
    project_details = get_input("Enter Your Project Details","alphabet_regex")
    # take project target amount
    project_target = get_input("Enter Your Project Target","positive_number_regex")
    # take project start date
    project_start_date = get_input("Enter Your Project Strat Date","date_regex")
    # take project end date
    project_end_date = get_input("Enter Your Project End Date","date_regex")
    # create the project
    project_data = Projects(logged_user.Email,project_title,project_details,project_target,project_start_date,project_end_date)
    project_data.add(index_file_path,data_file_path)
    # clean object for memory and security 
    del project_data
    system('clear')
    print("##############  Project Added ################")