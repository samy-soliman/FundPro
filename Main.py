# import regex library
import re
# import systym module
from  sys import exit
# import os
from os.path import exists as file_exists
from os import system

# import form
import Forms
##################### initialization #####################
# file path of our DB

file_path_data = "FundProData.txt"
file_path_index = "FundProIndex.txt"

# Open the file in append mode, which creates the file if it doesn't exist , and do not modify if exists
if not file_exists(file_path_data):
    with open(file_path_data, "a") as f:
        pass
if not file_exists(file_path_index):
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
            system('clear')
            break
        else:
            print("Wrong Input format, Please Enter a valid input")
    menu1_input=int(menu1_input)

    ## login option
    if menu1_input == 1:
        Forms.login_form(file_path_index,file_path_data)

    ## register option
    if menu1_input == 2:
        Forms.register_form(file_path_index,file_path_data)

    ## exit option
    if menu1_input == 3:
        print("########### Best ##### OF ###### LUCK ###############")
        print("##############       FUNDPRO         ################")
        print("####### it seems impossible until it's done #########")
        print("#####################################################")
        exit()
