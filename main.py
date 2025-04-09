


from db import db
from admin import Admin
from librarian import Librarian
from student import Student

def initialize_admin():
    """Ensures an admin account exists."""
    if db.execute_query("SELECT username FROM users WHERE role = 'admin'", fetch=True) is None:
        print("Welcome, Admin! Please set up your password.")
        admin_password = input("Set Admin Password: ")
        db.execute_query(
            "INSERT INTO users (username, password, role) VALUES ('admin', %s, 'admin')",
            (admin_password,)
        )
        print(" Admin account created successfully!")

def main():
    initialize_admin()
    
    print("\n Welcome to the Library Management System ")

    username = input("Enter username: ")
    password = input("Enter password: ")

    user = db.execute_query(
        "SELECT username, password, role FROM users WHERE username = %s",
        (username,),
        fetch=True
    )

    if not user:
        print(" Invalid username!")
        return

    stored_username, stored_password, role = user

    if password != stored_password:
        print(" Incorrect password!")
        return

    print(" Login successful!")

    if role == "admin":
        admin_menu(Admin(stored_username, stored_password))
    elif role == "librarian":
        librarian_menu(Librarian(stored_username, stored_password))
    elif role == "student":
        student_menu(Student(stored_username, stored_password))
    else:
        print(" Unknown role!")

def admin_menu(admin):
    """Admin functionality menu."""
    while True:
        print("\n Admin Menu:")
        print("1 Register Another Admin")
        print("2 Register Librarian")
        print("3 Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            admin.register_admin()
        elif choice == "2":
            admin.register_librarian()
        
        elif choice == "3":
            print(" Logging out...")
            break
        else:
            print(" Invalid choice!")

def librarian_menu(librarian):
    """Librarian functionality menu."""
    while True:
        print("\n Librarian Menu:")
        print("1 Register Student")
        print("2 Add Book")
        print("3 Remove Book")
        print("4 View Books")
        print("5 Logout")

        choice = input("Enter choice: ")
        
        if choice == "1":
            librarian.register_student() 
        elif choice == "2":
            librarian.add_book()    
        elif choice == "3":
            librarian.remove_book()
        elif choice == "4":
            librarian.view_books()
        elif choice == "5":
            print(" Logging out...")
            break
        else:
            print(" Invalid choice! Please try again.")

def student_menu(student):
    """Student functionality menu."""
    while True:
        print("\n Student Menu:")
        print("1 Borrow Book")
        print("2 Return Book")
        print("3 Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter book ID to borrow: ")
            student.borrow_book(book_id)
        elif choice == "2":
            book_id = input("Enter book ID to return: ")
            student.return_book(book_id)
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print(" Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
