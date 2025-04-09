from db import Database

db = Database()

class Student:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # Store password if needed

          # TO borrow the books
    def borrow_book(self, book_id):
        """Allows a student to borrow a book if available."""
        print(f"DEBUG: Attempting to borrow book with ID {book_id}")
        
        # Check if book exists and is available
        book = db.execute_query("SELECT available FROM books WHERE book_id = %s", (book_id,), fetch=True)

        if not book:
            print(" Book does not exist!")
            return
        
        if book[0] == 0:
            print("Book is not available!")
            return
        
        # Insert into borrowed_books
        try:
            db.execute_query("INSERT INTO borrowed_books (student_username, book_id) VALUES (%s, %s)", (self.username, book_id))
            db.execute_query("UPDATE books SET available = 0 WHERE book_id = %s", (book_id,))
            print(" Book borrowed successfully!")
        except Exception as e:
            print(f" Error borrowing book: {e}")
    
    def return_book(self, book_id):
        """Allows a student to return a borrowed book."""
        print(f"DEBUG: Attempting to return book with ID {book_id}")
        
        # Check if the student has borrowed this book
        record = db.execute_query("SELECT * FROM borrowed_books WHERE student_username = %s AND book_id = %s", (self.username, book_id), fetch=True)

        if not record:
            print(" You have not borrowed this book!")
            return
        
        # Delete from borrowed_books and mark as available
        try:
            db.execute_query("DELETE FROM borrowed_books WHERE student_username = %s AND book_id = %s", (self.username, book_id))
            db.execute_query("UPDATE books SET available = 1 WHERE book_id = %s", (book_id,))
            print(" Book returned successfully!")
        except Exception as e:
            print(f" Error returning book: {e}")
