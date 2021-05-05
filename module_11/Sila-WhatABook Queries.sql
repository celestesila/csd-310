/*
Celeste Sila
May 5, 2021
Module 11
WhatABook Queries
*/

--indicate database to be used
use whatabook;

--view users wish lists
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
INNER JOIN user ON wishlist.user_id = user.user_id
INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

--view stores
SELECT store_id, locale 
from store;

--view books
SELECT book_id, book_name, author, details 
from book;

--view books not on a wishlist
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (
    SELECT book_id 
    FROM wishlist 
    WHERE user_id = 1);

--add a book to a wishlist
INSERT INTO wishlist(user_id, book_id)
VALUES(1, 9);

--view users wish lists to verify addition of item
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
INNER JOIN user ON wishlist.user_id = user.user_id
INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

--delete added item from wishlist
DELETE FROM wishlist 
WHERE user_id = 1 AND book_id = 9;

--view users wish lists to verify deletion of added item
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
INNER JOIN user ON wishlist.user_id = user.user_id
INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;