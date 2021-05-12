/*
Celeste Sila
April 28, 2021
Module 10.3
WhatABook Database and Table Creation
*/

use whatabook; 

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to whatabook database to user 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

--Create tables
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

--insert store record 

INSERT INTO store(locale)
    VALUES('1110 S 71st St, Omaha, NE 68106 | Hours Mon-Sat 9A-9P Sun 11A-6P');

--insert book records 

INSERT INTO book(book_name, author)
    VALUES('To Kill a Mockingbord', 'Harper Lee');

INSERT INTO book(book_name, author)
    VALUES('Lord of the Flies', 'William Goldberg');

INSERT INTO book(book_name, author)
    VALUES('Slaughterhouse Five', 'Kurt Vonnegut');

INSERT INTO book(book_name, author)
    VALUES('Animal Farm', 'George Orwell');

INSERT INTO book(book_name, author, details)
    VALUES('Dune', 'Frank Herbert', 'Anniversary Edition');

INSERT INTO book(book_name, author)
    VALUES("Charlotte's Web", 'E.B. White');
 
INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');

INSERT INTO book(book_name, author)
    VALUES('Grapes of Wrath', 'John Steinbeck');

INSERT INTO book(book_name, author)
    VALUES('Frankenstein', 'Mary Shelley');

INSERT INTO book(book_name, author)
    VALUES('The Sound and the Fury', 'William Faulkner');

INSERT INTO book(book_name, author)
    VALUES('Fahrenheit 451', 'Ray Bradbury');

INSERT INTO book(book_name, author, details)
    VALUES('Zen and the Art of Motorcycle Maintenance', 'Robert Pirsig', 'Autographed Copy');

INSERT INTO book(book_name, author)
    VALUES('A Farwell to Arms', 'Ernest Hemmingway');

--insert user

INSERT INTO user(first_name, last_name) 
    VALUES('Johnny', 'Boi');

INSERT INTO user(first_name, last_name)
    VALUES('Gabby', 'Gyrl');

INSERT INTO user(first_name, last_name)
    VALUES('Randy', 'Rheadir');

--insert wishlist records 

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Johnny'), 
        (SELECT book_id FROM book WHERE book_name = 'Animal Farm')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Gabby'),
        (SELECT book_id FROM book WHERE book_name = 'Fahrenheit 451')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Johnny'),
        (SELECT book_id FROM book WHERE book_name = 'Lord of the Flies')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Randy'),
        (SELECT book_id FROM book WHERE book_name = 'Zen and the Art of Motorcycle Maintenance')
    );

