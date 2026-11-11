-- SQLite
--1. Obtenga todos los libros y sus autores (en caso de tenerlos)

SELECT books.Name, authors.Name FROM Books AS books
LEFT JOIN Authors AS authors 
ON books.Author = authors.ID;

--Obtenga todos los libros que no tienen autor

SELECT books.Name FROM Books AS books
LEFT JOIN Authors AS authors 
ON books.Author = authors.ID
WHERE authors.Name IS NULL;

-- Obtenga todos los autores que no tienen libros

SELECT authors.Name FROM Authors AS authors
LEFT JOIN Books AS books
ON authors.ID = books.Author
WHERE books.ID IS NULL;

--Obtenga todos los libros que han sido rentados en algún momento

SELECT DISTINCT books.Name FROM Books as books
INNER JOIN Rents as rents
ON books.ID = rents.BookID;

-- Obtenga todos los libros que nunca han sido rentados

SELECT DISTINCT books.Name FROM Books as books
LEFT JOIN Rents as rents
ON books.ID = rents.BookID
WHERE rents.BookID IS NULL;

--Obtenga todos los clientes que nunca han rentado un libro

SELECT DISTINCT customer.Name FROM Customers as customer
LEFT JOIN Rents as rents
ON customer.ID = rents.CustomerID
WHERE rents.CustomerID IS NULL;

--Obtenga todos los libros que han sido rentados y están en estado “Overdue” 

SELECT DISTINCT books.Name FROM Books as books
INNER JOIN Rents as rents
ON books.ID = rents.BookID 
WHERE rents.State = 'Overdue';