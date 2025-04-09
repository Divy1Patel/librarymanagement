# import mysql.connector

# class Database:
#     def __init__(self):
#         try:
#             self.conn = mysql.connector.connect(
#                 host="localhost",
#                 user="root",  # Change if needed
#                 password="Divya",  # Change to your actual MySQL password
#                 database="library_management",
#                 auth_plugin="mysql_native_password"
#             )
#             self.cursor = self.conn.cursor()
#             print(" Database connection successful!")
#         except mysql.connector.Error as e:
#             print(f" Error connecting to database: {e}")

#     def execute_query(self, query, values=None):
#         try:
#             self.cursor.execute(query, values or ())
#             self.conn.commit()
#         except mysql.connector.Error as e:
#             print(f" Error executing query: {e}")

#     def fetch_one(self, query, values=None):
#         self.cursor.execute(query, values or ())
#         return self.cursor.fetchone()

#     def fetch_all(self, query, values=None):
#         self.cursor.execute(query, values or ())
#         return self.cursor.fetchall()

#     def close_connection(self):
#         self.cursor.close()
#         self.conn.close()
#         print(" Database connection closed.")
    

#     def view_books(self):
#         query = "SELECT book_id, title, author, available FROM books"
#         result = self.fetch_all(query)
#         if result:
#             print("\n Available Books:")
#             print("-" * 50)
#             for book in result:
#                 book_id, title, author, available = book
#                 status = " Available" if available else " Borrowed"
#                 print(f" {book_id} | {title} | {author} | {status}")
#             print("-" * 50)
#         else:
#             print("\n No books available.")
    

# #   To Ensure 'borrowed_books' table has 'student_username'
# db = Database()
# db.execute_query("""
#     ALTER TABLE borrowed_books 
#     ADD COLUMN student_username VARCHAR(255) NOT NULL AFTER book_id;
# """)
# db.execute_query("""
#     ALTER TABLE borrowed_books 
#     ADD FOREIGN KEY (student_username) REFERENCES users(username);
# """)
# print(" Database schema updated successfully!")
import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="Divya", 
                database="library_management",
                auth_plugin="mysql_native_password"
            )
            self.cursor = self.conn.cursor(buffered=True)
        except mysql.connector.Error as e:
            print(f"Database error: {e}")

    def execute_query(self, query, values=None, fetch=False, fetch_all=False):
        try:
            self.cursor.execute(query, values or ())
            if fetch:
                result = self.cursor.fetchone()  # Fetch one row
                self.cursor.fetchall()  # Clear remaining results
                return result
            if fetch_all:
                return self.cursor.fetchall()
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Query error: {e}")

    def close(self):
        self.cursor.close()
        self.conn.close()
# Create a global instance for use
db = Database()