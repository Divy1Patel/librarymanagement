from user import User
from student import Student
from db import Database

db = Database()

class Librarian(User):
    def __init__(self, username, password):
        super().__init__(username, password, "librarian")

    def register_student(self):
        username = input("Enter new student username: ")
        if db.fetch_one("SELECT username FROM users WHERE username = %s", (username,)):
            print("User already exists!")
            return
        
        password = input("Enter password: ")
        db.execute_query("INSERT INTO users (username, password, role) VALUES (%s, %s, 'student')", (username, password))
        print(f"Student '{username}' registered successfully!")

    def view_books(self):
        """Fetch and display all books in the library."""
        books = db.fetch_all("SELECT book_id, title, author, available FROM books")  # Fetch books
        
        if not books:
            print(" No books available in the library.")
            return  

        print("\n Available Books:")
        for book in books:
            status = "Available" if book[3] else "Not Available"
            print(f"🔹 ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {status}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        db.execute_query("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        print(f"Book '{title}' added successfully!")

    def remove_book(self):
        book_id = input("Enter book ID to remove: ")
        if db.fetch_one("SELECT book_id FROM books WHERE book_id = %s", (book_id,)):
            db.execute_query("DELETE FROM books WHERE book_id = %s", (book_id,))
            print("Book removed successfully!")
        else:
            print("Book not found!")
