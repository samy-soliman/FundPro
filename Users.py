# user class, it should provide all operations on our user
class Users:
    # initialize the user with its data
    def __init__(self, First_name, Last_name, Email,Password,Phone):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Email = Email
        self.Password = Password
        self.Phone = Phone
    
    # save user to file
    def register(self):
        pass

    # delete user from file
    def delete(self):
        pass

    # validate user
    def login(self):
        pass
    



