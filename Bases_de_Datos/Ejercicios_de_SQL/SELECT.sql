-- SQLite
SELECT * FROM Products;
SELECT * FROM Products WHERE Price > 50000;
SELECT * FROM Products_Per_Invoice WHERE Product_Code_id = 2; -- Obtenga todas las compras de un mismo producto por id. este no me quedo muy claro
SELECT Product_Code_id, sum(Total_amount) FROM Products_Per_Invoice GROUP BY Product_Code_id;
SELECT Invoice_Number FROM Invoice where Buyer_email = 'juan@gmail.com';
SELECT Invoice_Number, Total_amount FROM Invoice ORDER BY Total_amount DESC;
SELECT * from Invoice where invoice_Number = 3;
