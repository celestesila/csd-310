""" 
    Name:  Celeste Sila
    Date:  May 9, 2021
    Module:  11.2
    Title: WhatABook
    Description: First draft of WhatABook 
"""
import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#  display main menu and obtain input selection
def show_menu():
    print("\nMain Menu\n")

    print("\t1.\tView Books\n\t2.\tView Store Locations\n\t3.\tMy Account\n\t4.\tExit Program")

    try:
        choice = int(input('\nPlease enter a selection of 1-4 from the Main Menu above:\t'))

        return choice
    except ValueError:
        
        print("\n***You have made an invalid selection.  Please try again.***")
        user_selection = show_menu()

def show_books(_cursor):

    #  retrieve and display all book information
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()

    print("\n\t--- BOOKS ---\n") 
    for book in books:
        print("\tBook ID:  {}\n\t\tBook Name:\t{}\n\t\tAuthor:\t\t{}\n\t\tDetails:\t{}\n".format(book[0], book[1], book[2], book[3]))

def show_locations(_cursor):

    #  retrieve and display all location information
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n\t--- STORE LOCATIONS ---\n")

    for location in locations:
        print("\t{}\n".format(location[1]))

def validate_user():
    
    #  input and validate customer id
    try:
        user_id = int(input('\n\t--- MY ACCOUNT ---\n\n\tPlease enter your user id:\t'))

        if user_id <= 0 or user_id > 3:
                        
            print("\n\t***You have entered an invalid user id.  Please try again.***")

            validate_user()

        return user_id
    except ValueError:

            print("\n\t***You have entered an invalid user id.  Please try again.***")

            validate_user()

def show_account_menu():
    
    #  display account menu and obtain input selection 
    try:
        print("\n\tAccount Menu")
        print("\n\t1.\tWishlist\n\t2.\tAdd Book\n\t3.\tMain Menu")
        account_option = int(input('\n\tPlease enter a selection of 1-3 from the Account Menu above:\t'))

        return account_option
    except ValueError:
        
        print("\n\t***You have made an invalid selection.  Please try again.***")
        account_option = show_account_menu()

def show_wishlist(_cursor, _user_id):
    
    #  retrieve and display all books on the customer's wishlist
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n\t\t- Your Wishlist -")

    for book in wishlist:
        print("\n\t\tBook Name:\t{}\n\t\tAuthor:\t\t{}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    
    #  retrieve and display all books not on the customer's wishlist plus obtain add input
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n\t\t- Available Books -")

    for book in books_to_add:
        print("\n\t\tBook Id:\t{}\n\t\tBook Name:\t{}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    #  connect to database
    db = mysql.connector.connect(**config) 

    #  cursor for MySQL queries
    cursor = db.cursor() 

    #  output welcome message
    print("\n*** Welcome to WhatABook! ***")
    
    #  show main menu
    user_selection = show_menu()  

    #  while loop for Main Menu selection not equal to 4
    while user_selection != 4:

        #  selection equals 1 call the show_books method
        if user_selection == 1:
            show_books(cursor)

        #  selection equals 2 call the show_locations method 
        if user_selection == 2:
            show_locations(cursor)

        #  selection equals 3 call the validate_user method 
        #    if id is valid call the show_account_menu method
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #  while loop for account selection does not equal 3
            while account_option != 3:

                #  selection equals 1 call the show_wishlist() method  
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #  select equals 2 call the show_books_to_add function 
                if account_option == 2:

                    #  display books not on wishlist
                    show_books_to_add(cursor, my_user_id)

                    #  obtain book id input 
                    book_id = int(input("\n\t\tPlease enter the Book Id from above that you wish to add to your list:\t"))
                    
                    #  add book to wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #  commit changes
                    db.commit() 

                    #  output successful message  
                    print("\n\t\tBook id {} was successfully added to your wishlist.".format(book_id))

                #  selection less than or equal to 0 or greater than 3 error 
                if account_option <= 0 or account_option > 3:
                    print("\n\t***You have made an invalid selection.  Please try again.***")

                #  display account menu 
                account_option = show_account_menu()
        
        #  selection is less than or equal to 0 or greater than 4 error
        if user_selection <= 0 or user_selection > 4:
            print("\n***You have made an invalid selection.  Please try again.***")
            
        # display main menu
        user_selection = show_menu()

    #  output good bye message
    print("\n\tYou are now leaving WhatABook.\n\tPlease visit again soon.\n\tThank you and have a great day.\n")

except mysql.connector.Error as err:
 
    #  error handling
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\tThe username or password entered is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\tThe database entered is invalid.")

    else:
        print(err)

finally:    
    #  close MySQL connection
    db.close()
