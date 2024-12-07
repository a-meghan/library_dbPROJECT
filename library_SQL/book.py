from connect_mysql import connect_database
conn, cursor = connect_database()

# Book Class
class Book:
    def __init__(self, id, title, author_id, genre, publication_date, availability_status):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = availability_status

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author_id

    def get_genre(self):
        return self.genre

    def get_publication_date(self):
        return self.publication_date

    def get_availability_status(self):
        return self.availability_status

    def set_availability_status(self, status):
        self.availability_status = status

# Book Menu Functions
def add_book(conn, cursor):
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    query = "INSERT INTO books (title, author_id, genre, publication_date, availability_status) VALUES (%s, %s, %s, %s, 'Available')"
    cursor.execute(query, (title, author_id, genre, publication_date))
    conn.commit()
    print("Book added successfully!")

def borrow_book(conn, cursor):
    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    book = cursor.fetchone()
    if book and book[5] == 'Available':
        query = "INSERT INTO borrowed_books (user_id, book_id) VALUES (%s, %s)"
        cursor.execute(query, (user_id, book_id))
        query = "UPDATE books SET availability_status = 'Borrowed' WHERE id = %s"
        cursor.execute(query, (book_id,))
        conn.commit()
        print("Book borrowed successfully!")
    else:
        print("Book is not available.")

def return_book(conn, cursor):
    book_id = input("Enter book ID: ")
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM borrowed_books WHERE user_id = %s AND book_id = %s"
    cursor.execute(query, (user_id, book_id))
    borrowed_book = cursor.fetchone()
    if borrowed_book:
        query = "DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s"
        cursor.execute(query, (user_id, book_id))
        query = "UPDATE books SET availability_status = 'Available' WHERE id = %s"
        cursor.execute(query, (book_id,))
        conn.commit()
        print("Book returned successfully!")
    else:
        print("Book is not borrowed.")

def search_book(conn, cursor):
    title = input("Enter book title: ")
    query = "SELECT * FROM books WHERE title = %s"
    cursor.execute(query, (title,))
    book = cursor.fetchone()
    if book:
        print("Book details:")
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("Publication Date:", book[4])
    else:
        print("Book not found.")

def display_all_books(conn, cursor):
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    print("All books:")
    for book in books:
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("Publication Date:", book[4])