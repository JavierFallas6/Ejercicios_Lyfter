-- SQLite
--1. Obtenga todos los libros y sus autores (en caso de tenerlos)

SELECT B.Name, A.Name FROM Books AS B
LEFT JOIN Authors AS A 
ON B.Author = A.ID;

--Obtenga todos los libros que no tienen autor

SELECT B.Name FROM Books AS B
LEFT JOIN Authors AS A 
ON B.Author = A.ID
WHERE A.Name IS NULL;

-- Obtenga todos los autores que no tienen libros

SELECT A.Name FROM Authors AS A
LEFT JOIN Books AS B
ON A.ID = B.Author
WHERE B.ID IS NULL;

--Obtenga todos los libros que han sido rentados en algún momento

SELECT DISTINCT B.Name FROM Books as B
INNER JOIN Rents as R
ON B.ID = R.BookID

-- Obtenga todos los libros que nunca han sido rentados

SELECT DISTINCT B.Name FROM Books as B
LEFT JOIN Rents as R
ON B.ID = R.BookID
WHERE R.BookID IS NULL;

--Obtenga todos los clientes que nunca han rentado un libro

SELECT DISTINCT C.Name FROM Customers as C
LEFT JOIN Rents as R
ON C.ID = R.CustomerID
WHERE R.CustomerID IS NULL;

--Obtenga todos los libros que han sido rentados y están en estado “Overdue” 

SELECT DISTINCT B.Name FROM Books as B
INNER JOIN Rents as R
ON B.ID = R.BookID 
WHERE R.State = 'Overdue'