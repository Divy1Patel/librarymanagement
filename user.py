from db import db  

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user_data = db.fetch_one("SELECT username, password, role FROM users WHERE username = %s", (username,))
        
        if user_data:
            stored_username, stored_password, stored_role = user_data
            
            if password == stored_password:  #  Ensure password checking is correct
                print(f"Login successful as {stored_role}!")
                return stored_role
            else:
                print("Invalid password!")
        else:
            print("User not found!")

        return None
