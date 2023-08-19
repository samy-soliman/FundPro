#################### Importing packages #####################
# import regex library
from re import match
# import os
from os import system

# import form
import Forms
# import application variables
from AppEnvs import AppEnvs
# import Project class
from  Projects import Projects
################### End Of Imports ##########################

##################### Start Of Initialization ########################
AppEnvs.init_files()
# create a user for session info
logged_user = None
#################### End Of Initilization #####################

##################### Start Program Execute ###################

##################### Start Main Menu ###################
# welcome message
print("#####################################################")
print("welcome to fundpro website,  where dreams become true")
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
        if match("^[1-3]{1}$", menu1_input):
            system('clear')
            break
        else:
            print("Wrong Input format, Please Enter a valid input")
    menu1_input=int(menu1_input)

    ## login option
    if menu1_input == 1:
        logged_user = Forms.login_form(AppEnvs.file_path_users_index,AppEnvs.file_path_users_data)
        system('clear')
        break

    ## register option
    if menu1_input == 2:
        Forms.register_form(AppEnvs.file_path_users_index,AppEnvs.file_path_users_data)

    ## exit option
    if menu1_input == 3:
        Forms.exit_main_form()
##################### End Main Menu ###################

##################### Start Projects Menu ###################
# Start Program project menu (menu2)
# start a loop until a valid input is taken or exit

# start Menu after login
print("Welcome " + logged_user.First_name)
while True:
    while True:
        print("Enter Your Option Number: ")
        print("1) Create Project")
        print("2) View Projects")
        print("3) Edit Projects")
        print("4) Delete Projects")
        print("5) Search Projects")
        print("6) Exit")
        menu2_input = input()
        if match("^[1-6]{1}$", menu2_input):
            system('clear')
            break
        else:
            print("Wrong Input format, Please Enter a valid input")
    menu2_input=int(menu2_input)

    ## create project option
    if menu2_input == 1:
        Forms.create_project_form(AppEnvs.file_path_projects_index,AppEnvs.file_path_projects_data,logged_user)

    ## List option
    if menu2_input == 2:
        Projects.get_projects(AppEnvs.file_path_projects_data)
    ## edit option
    if menu2_input == 3:
        pass
    ## delete option
    if menu2_input == 4:
        pass
    ## search option
    if menu2_input == 5:
        print("Enter Your Date")
        search_project_date = input()
        Projects.search_projects(AppEnvs.file_path_projects_data,"StartDate",search_project_date)
    ## exit option
    if menu2_input == 6:
        Forms.exit_main_form()
##################### End Projects Menu ###################

##################### End Program Execute ###################
