from db import Database

db = Database()
print("Fetching all users...")
users = db.fetch_all("SELECT * FROM users")
print(users)
