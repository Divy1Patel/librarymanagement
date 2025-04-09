from db import db  
from user import User  

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def register_librarian(self):
        username = input("Enter new librarian username: ")  
        if db.execute_query("SELECT username FROM users WHERE username = %s", (username,),fetch=True):
            print("User already exists!")
            return  

        password = input("Enter password: ")  
        db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, 'librarian')", (username, password))
        print(f"Librarian '{username}' registered successfully!")  

    def register_admin(self):
        """Allow an existing admin to register a new admin."""
        username = input("Enter new admin username: ")  
        if db.execute_query("SELECT username FROM users WHERE username = %s", (username,),fetch=True):
            print("Admin already exists!")
            return  

        password = input("Enter password: ")  
        db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, 'admin')", (username, password))
        print(f"Admin '{username}' registered successfully!")  
