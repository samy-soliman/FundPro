# This files containes our program main variables and behaviours 
from os.path import exists as file_exists

class AppEnvs:
    # files path of our users data
    file_path_users_data = "FundProUsersData.txt"
    file_path_users_index = "FundProUsersIndex.txt"

    # files path of our users projects
    file_path_projects_data = "FundProProjectsData.txt"
    file_path_projects_index = "FundProProjectsIndex.txt"

    @staticmethod
    def init_files():
        # Open the file in append mode, which creates the file if it doesn't exist , and do not modify if exists
        if not file_exists(AppEnvs.file_path_users_data):
            with open(AppEnvs.file_path_users_data, "a") as f:
                pass
        if not file_exists(AppEnvs.file_path_users_index):
            with open(AppEnvs.file_path_users_index, "a") as f:
                pass
        if not file_exists(AppEnvs.file_path_projects_data):
            with open(AppEnvs.file_path_projects_data, "a") as f:
                pass
        if not file_exists(AppEnvs.file_path_projects_index):
            with open(AppEnvs.file_path_projects_index, "a") as f:
                pass