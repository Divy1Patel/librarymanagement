# from user import User
# from student import Student
# from db import Database

# db = Database()

# class Librarian(User):
#     def __init__(self, username, password):
#         super().__init__(username, password, "librarian")

#     def register_student(self):
#         username = input("Enter new student username: ")
#         if db.fetch_one("SELECT username FROM users WHERE username = %s", (username,)):
#             print("User already exists!")
#             return
        
#         password = input("Enter password: ")
#         db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, 'student')", (username, password))
#         print(f"Student '{username}' registered successfully!")

#     def view_books(self):
#         """Fetch and display all books in the library."""
#         books = db.fetch_all("SELECT book_id, title, author, available FROM books")  # Fetch books
        
#         if not books:
#             print(" No books available in the library.")
#             return  

#         print("\n Available Books:")
#         for book in books:
#             status = "Available" if book[3] else "Not Available"
#             print(f"🔹 ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {status}")

#     def add_book(self):
#         title = input("Enter book title: ")
#         author = input("Enter book author: ")
#         db.execute_query("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
#         print(f"Book '{title}' added successfully!")

#     def remove_book(self):
#         book_id = input("Enter book ID to remove: ")
#         if db.fetch_one("SELECT book_id FROM books WHERE book_id = %s", (book_id,)):
#             db.execute_query("DELETE FROM books WHERE book_id = %s", (book_id,))
#             print("Book removed successfully!")
#         else:
#             print("Book not found!")
from db import db
from user import User  # Ensure User class is properly defined

class Librarian(User):
    def __init__(self, username, password):
        super().__init__(username, password, "librarian")

    def register_student(self):
        """Registers a new student in the system."""
        username = input("Enter new student username: ")
        if db.execute_query("SELECT username FROM users WHERE username = %s", (username,), fetch=True):
            print("User already exists!")
            return
        
        password = input("Enter password: ")
        db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, 'student')", (username, password))
        print(f" Student '{username}' registered successfully!")

    def view_books(self):
        """Fetch and display all books in the library."""
        books = db.execute_query("SELECT book_id, title, author, available FROM books", fetch_all=True)

        if not books:
            print("\n No books available in the library.")
            return  

        print("\n Available Books:")
        print("-" * 50)
        for book in books:
            status = " Available" if book[3] else " Not Available"
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")
        print("-" * 50)

    def add_book(self):
        """Adds a new book to the library."""
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        db.execute_query("INSERT INTO books (title, author, available) VALUES (%s, %s, 1)", (title, author))
        print(f" Book '{title}' added successfully!")

    def remove_book(self):
        """Removes a book from the library."""
        book_id = input("Enter book ID to remove: ")
        if db.execute_query("SELECT book_id FROM books WHERE book_id = %s", (book_id,), fetch=True):
            db.execute_query("DELETE FROM books WHERE book_id = %s", (book_id,))
            print(" Book removed successfully!")
        else:
            print(" Book not found!")

