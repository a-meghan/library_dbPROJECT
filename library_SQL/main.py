from connect_mysql import connect_database
conn, cursor = connect_database()
from book import add_book, borrow_book, return_book, search_book, display_all_books
from user import add_user, view_user_details, display_all_users
from author import add_author, view_author_details, display_all_authors


def main_menu():
    while True:
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            book_operations_menu(conn, cursor)
        elif main_choice == "2":
            user_operations_menu(conn, cursor)
        elif main_choice == "3":
            author_operations_menu(conn, cursor)
        elif main_choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations_menu(conn, cursor):
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

    book_op_choice = input("Enter your choice: ")
    if book_op_choice == "1":
        add_book(conn, cursor)
    elif book_op_choice == "2":
        borrow_book(conn, cursor)
    elif book_op_choice == "3":
        return_book(conn, cursor)
    elif book_op_choice == "4":
        search_book(conn, cursor)
    elif book_op_choice == "5":
        display_all_books(conn, cursor)
    else:
        print("Invalid choice. Please try again.")
        book_operations_menu(conn, cursor)

def user_operations_menu(conn, cursor):
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

    user_op_choice = input("Enter your choice: ")

    if user_op_choice == "1":
        add_user(conn, cursor)
    elif user_op_choice == "2":
        view_user_details(conn, cursor)
    elif user_op_choice == "3":
        display_all_users(conn, cursor)
    else:
        print("Invalid choice. Please try again.")
        user_operations_menu(conn, cursor)

def author_operations_menu(conn, cursor):
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

    author_op_choice = input("Enter your choice: ")

    if author_op_choice == "1":
        add_author(conn, cursor)
    elif author_op_choice == "2":
        view_author_details(conn, cursor)
    elif author_op_choice == "3":
        display_all_authors(conn, cursor)
    else:
        print("Invalid choice. Please try again.")
        author_operations_menu(conn, cursor)

if __name__ == "__main__":
    main_menu()