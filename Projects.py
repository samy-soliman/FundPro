import json
from prettytable import PrettyTable

def append_data(data, index_file_path, data_file_path):
    with open(data_file_path, "a") as data_file:
        position = data_file.tell()  # Get the current file position (end of the file)
        json.dump(data, data_file)
        data_file.write("\n")  # Add a newline to separate entries

    # Update the index file with the new entry's position
    with open(index_file_path, "a") as index_file:
        index_file.write(f"{data['Title']}:{position}\n")

def delete_entry(key, index_file_path, data_file_path):
    # Delete the entry from the data file
    with open(data_file_path, "r") as data_file:
        lines = data_file.readlines()

    with open(data_file_path, "w") as data_file:
        for line in lines:
            data = json.loads(line.strip())
            if data["key"] != key:
                data_file.write(json.dumps(data) + "\n")

    # Delete the entry from the index file
    with open(index_file_path, "r") as index_file:
        lines = index_file.readlines()

    with open(index_file_path, "w") as index_file:
        for line in lines:
            index_key, _ = line.strip().split(":")
            if index_key != key:
                index_file.write(line)

# project class, it should provide all operations on our project
class Projects:
    # initialize the project with its data
    def __init__(self,Email,Title,Details,Target,StartDate,EndDate):
        self.Email = Email
        self.Title = Title
        self.Details = Details
        self.Target = Target
        self.StartDate = StartDate
        self.EndDate = EndDate
    
    @staticmethod
    def get_project_data(index_file_path, data_file_path, key):
        with open(index_file_path, "r") as index_file:
            for line in index_file:
                index_key, position = line.strip().split(":")
                if index_key == key:
                    with open(data_file_path, "r") as data_file:
                        data_file.seek(int(position))  # Move to the specified position in the data file
                        data_line = data_file.readline().strip()
                        return json.loads(data_line)  # Deserialize the JSON data
        return None  # Key not found in the index
    
    @staticmethod
    def get_projects(data_file_path):
        # Read the file line by line and parse each line as JSON
        data = []
        with open(data_file_path, 'r') as file:
            for line in file:
                try:
                    dictionary = json.loads(line.strip())
                    data.append(dictionary)
                except json.JSONDecodeError:
                    print(f"Error parsing line: {line}")

        # Create a PrettyTable
        table = PrettyTable()
        if data:
            # Add table headers
            table.field_names = data[0].keys()

            # Add rows to the table
            for dictionary in data:
                table.add_row(dictionary.values())

            # Print the table
            print(table)
        else:
            print("No data found in the file.")
    
    @staticmethod
    def search_projects(data_file_path,key,value):
        data = []
        with open(data_file_path, "r") as json_file:
            for line in json_file:
                line_data = json.loads(line)
                if line_data.get(key) == value:
                    data.append(line_data)
        
        # Create a PrettyTable
        table = PrettyTable()
        if data:
            # Add table headers
            table.field_names = data[0].keys()

            # Add rows to the table
            for dictionary in data:
                table.add_row(dictionary.values())

            # Print the table
            print(table)
        else:
            print("No data found in the file.")
    # save project to file
    def add(self,index_file_path,data_file_path):
        append_data(self.__dict__, index_file_path,data_file_path)

    # delete project from file
    def delete(self):
        pass
        # Delete an entry
        # key_to_delete = "key"
        # delete_entry(key_to_delete, data_file_path, index_file_path)



