# User class
class User:
    def __init__(self, id, name, library_id):
        self.id = id
        self.name = name
        self.library_id = library_id

    def get_name(self):
        return self.name

    def get_library_id(self):
        return self.library_id

# User Menu Functions
def add_user(conn, cursor):
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
    cursor.execute(query, (name, library_id))
    conn.commit()
    print("User added successfully!")

def view_user_details(conn, cursor):
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user:
        print("User details:")
        print("Name:", user[1])
        print("Library ID:", user[2])
    else:
        print("User not found.")

def display_all_users(conn, cursor):
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    print("All users:")
    for user in users:
        print("Name:", user[1])
        print("Library ID:", user[2])