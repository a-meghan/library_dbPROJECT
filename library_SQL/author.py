from connect_mysql import connect_database
conn, cursor = connect_database()

# Author Class
class Author:
    def __init__(self, id, name, biography):
        self.id = id
        self.name = name
        self.biography = biography

    def get_name(self):
        return self.name

    def get_biography(self):
        return self.biography


# Author Menu Functions
def add_author(conn, cursor):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, biography))
    conn.commit()
    print("Author added successfully!")

def view_author_details(conn, cursor):
    author_id = input("Enter author ID: ")
    query = "SELECT * FROM authors WHERE id = %s"
    cursor.execute(query, (author_id,))
    author = cursor.fetchone()
    if author:
        print("Author details:")
        print("Name:", author[1])
        print("Biography:", author[2])
    else:
        print("Author not found.")

def display_all_authors(conn, cursor):
    query = "SELECT * FROM authors"
    cursor.execute(query)
    authors = cursor.fetchall()
    print("All authors:")
    for author in authors:
        print("Name:", author[1])
        print("Biography:", author[2])