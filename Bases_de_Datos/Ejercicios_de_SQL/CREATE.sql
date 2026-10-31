-- SQLite
CREATE TABLE Products (
Code INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(50) NOT NULL,
Price DECIMAL(8,2) NOT NULL,
Entry_Date DATE NOT NULL,
Brand VARCHAR(25) NOT NULL,
Stock_available INT NOT NULL  
);

CREATE TABLE Invoice (
Invoice_Number INT NOT NULL PRIMARY KEY,
Purchase_Date DATE NOT NULL,
Buyer_email VARCHAR(50) NOT NULL,
Total_amount DECIMAL(8,2) NOT NULL
);

CREATE TABLE Products_Per_Invoice (
Quantity INT NOT NULL,
Total_amount DECIMAL(8,2) NOT NULL,
Invoice_Number_id INT REFERENCES Invoice(Invoice_Number),
Product_Code_id INT REFERENCES Products(Code)
);

CREATE TABLE Shopping_Cart (
Buyer_email VARCHAR(50) NOT NULL,
Products VARCHAR(50) NOT NULL PRIMARY KEY
);

CREATE TABLE Products_Per_Shopping_Cart (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
Products VARCHAR(50) NOT NULL REFERENCES Shopping_Cart(Products),
Product_Code_id INT NOT NULL REFERENCES Products(Code)
);

