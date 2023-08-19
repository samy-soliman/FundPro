import json


def append_data(data, index_file_path, data_file_path):
    with open(data_file_path, "a") as data_file:
        position = data_file.tell()  # Get the current file position (end of the file)
        json.dump(data, data_file)
        data_file.write("\n")  # Add a newline to separate entries

    # Update the index file with the new entry's position
    with open(index_file_path, "a") as index_file:
        index_file.write(f"{data['Email']}:{position}\n")

def delete_user(key, index_file_path, data_file_path):
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

# user class, it should provide all operations on our user
class Users:
    # initialize the user with its data
    def __init__(self, First_name,Last_name,Email,Password,Phone):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Email = Email
        self.Password = Password
        self.Phone = Phone
    
    @staticmethod
    def get_user_data(index_file_path, data_file_path, key):
        with open(index_file_path, "r") as index_file:
            for line in index_file:
                index_key, position = line.strip().split(":")
                if index_key == key:
                    with open(data_file_path, "r") as data_file:
                        data_file.seek(int(position))  # Move to the specified position in the data file
                        data_line = data_file.readline().strip()
                        return json.loads(data_line)  # Deserialize the JSON data
        return None  # Key not found in the index
    
    # save user to file
    def register(self,index_file_path,data_file_path):
        append_data(self.__dict__, index_file_path,data_file_path)

    # delete user from file
    def delete(self):
        pass
        # Delete an entry
        # key_to_delete = "key"
        # delete_entry(key_to_delete, data_file_path, index_file_path)



