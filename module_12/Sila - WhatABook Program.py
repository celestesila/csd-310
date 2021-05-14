""" 
    Name:  Celeste Sila
    Date:  May 14, 2021
    Module:  12
    Title: WhatABook
    Description: WhatABook program to provide customers the ability to view all book, store locations, 
    and access account to view wishlist and add to wishlist.
"""
#  import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#  configure database objects
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#  display main menu and obtain menu selection
def show_menu():
 
    print("\nMain Menu\n\n\t1.\tView Books\n\t2.\tView Store Locations\n\t3.\tMy Account\n\t4.\tExit Program")
      
    menu_selection = input("\nPlease enter a selection of 1-4 from the Main Menu above:\t")

    while menu_selection not in ("1", "2", "3", "4"):
        menu_selection = input("\n***You have entered an invalid selection.***\n\nPlease enter a selection of 1-4 from the Main Menu above:\t")

    if menu_selection == "1":
        show_books(cursor)

    if menu_selection == "2":
        show_locations(cursor)

    if menu_selection == "3":
        user_id = validate_user(cursor)
        show_account_menu(cursor, user_id)

    if menu_selection == "4":
        print("\n\tYou are now leaving WhatABook.\n\tPlease visit again.\n")
        exit()

#  retrieve and display all book information
def show_books(_cursor):

    print("\n\t--- BOOKS ---\n")
    
    cursor.execute("SELECT book_id, book_name, author, details " +
                    "FROM book ORDER BY book_id")

    books = cursor.fetchall()
    for book in books:
        print("\tBook ID:  {}\n\t\tBook Name:\t{}\n\t\tAuthor:\t\t{}\n\t\tDetails:\t{}\n".format(book[0], book[1], book[2], book[3]))

    show_menu() 

#  retrieve and display all location information
def show_locations(_cursor):

    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n\t--- STORE LOCATIONS ---\n")

    for location in locations:
        print("\t{}\n".format(location[1]))
    
    show_menu() 

#  input and validate customer id
def validate_user(cursor):
    
    print ('\n\t--- MY ACCOUNT ---\n')

    cursor.execute("SELECT user_id FROM user")
    user_id_list = []
    query_results = cursor.fetchall()
    for row in query_results:
        user_id_list.append(str(row[0])) 

    user_id = input("\tPlease enter your user id:\t ")

    while (user_id not in user_id_list):
        user_id = input("\n\t***You have entered an invalid user id.***\n\n\tPlease enter a valid user id:\t ")

    return user_id

#  display account menu and obtain input selection 
def show_account_menu(cursor, user_id):
    
    cursor.execute("SELECT first_name FROM user" +
                    " WHERE user_id = " + str(user_id))
    first_name = cursor.fetchall()
    
    print("\n\tAccount Menu\n\n\t1.\tWishlist\n\t2.\tAdd Book\n\t3.\tMain Menu")

    menu_selection = input("\n\tPlease enter a selection of 1-3 from the Account Menu above:\t")
    
    while menu_selection not in ("1", "2", "3"):
        menu_selection = input("\n\t***You have made an invalid selection.***\n\n\tPlease enter a valid selection from the Account Menu:\t")

    if menu_selection == "1":
        show_wishlist(cursor, user_id)
    
    if menu_selection == "2":
        book_id = show_books_to_add(cursor, user_id)
        add_book_to_wishlist(cursor, user_id, book_id)
    
    if menu_selection == "3":
        show_menu()

#  retrieve and display all books on the customer's wishlist
def show_wishlist(cursor, user_id):
    
    print("\n\t\t- Your Wishlist -")
    
    cursor.execute("SELECT book.book_name, book.author" +
                    " FROM book" +
                    " INNER JOIN wishlist ON book.book_id = wishlist.book_id" +
                    " INNER JOIN user ON wishlist.user_id = user.user_id" +
                    " WHERE user.user_id = " + user_id)

    user_wishlist = cursor.fetchall()
    
    for row in user_wishlist:
        print(f"\n\t\tTitle:\t\t{row[0]}")
        print(f"\t\tAuthor:\t\t{row[1]}\n")

    show_account_menu(cursor, user_id)

#  retrieve and display all books not on the customer's wishlist plus obtain add input
def show_books_to_add(cursor, user_id):
    
    print("\n\t\t- Available Books -")

    cursor.execute("SELECT book_id, book_name, author, details FROM book" +
                    " WHERE book_id NOT IN (SELECT book_id FROM wishlist" +
                    " WHERE user_id = " + str(user_id) + ")" +
                    " ORDER BY book_id")
    
    books_to_add = cursor.fetchall()

    for book in books_to_add:
        print(f"\n\t\tBook Id:    {book[0]}")
        print(f"\t\t\tTitle:\t\t{book[1]}")
        print(f"\t\t\tAuthor:\t\t{book[2]}")
        print(f"\t\t\tDetails:\t{book[3]}\n")

    books_to_add_ids = []
    for book in books_to_add:
        books_to_add_ids.append(str(book[0]))

    book_id = input("\n\t\tEnter the Book Id from above that you wish to add to your list or x to return to the Account Menu:\t")
         
    while book_id not in books_to_add_ids and book_id.lower() != "x":
        book_id = input("\n\t\t***You have made an invalid selection.***\n\n\t\tEnter a valid book id or x to return to the Account Menu:\t")

    if book_id.lower() == "x":
        show_account_menu(cursor, user_id)
    else:
        return book_id

#  add book to wishlist
def add_book_to_wishlist(cursor, user_id, book_id):

    cursor.execute("INSERT INTO wishlist (user_id, book_id)" + "VALUES (" + user_id + ", " + book_id + ")")

    db.commit()

    cursor.execute("SELECT book_name FROM book WHERE book_id = " + book_id)
    book_names = cursor.fetchall()
    
    for row in book_names:
        book_name = row[0]

    print ("\n\t\tBook id {}: {} was successfully added to your wishlist.".format(book_id, book_name))

    show_account_menu(cursor, user_id) 
       
try:
    # connect to database
    db = mysql.connector.connect(**config)

    # cursor for MySQL queries
    cursor = db.cursor()
    
    # display Main Menu
    show_menu()


# error handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\tInvalid username or password.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\tInvalid database.")

    else:
        print(err)

# close database connection
finally:
    
    db.close()