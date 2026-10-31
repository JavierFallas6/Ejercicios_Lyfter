-- SQLite
SELECT * FROM Products;
SELECT * FROM Products WHERE Price > 50000;
SELECT * FROM Products_Per_Invoice WHERE Product_Code_id = 0; -- Obtenga todas las compras de un mismo producto por id. este no me quedo muy claro
SELECT Product_Code_id, sum(Total_amount) FROM Products_Per_Invoice GROUP BY Product_Code_id;
SELECT Invoice_Number FROM Invoice GROUP BY Buyer_email;
SELECT Invoice_Number, Total_amount FROM Invoice ORDER BY Total_amount DESC;
SELECT DISTINCT(invoice_Number) from Invoice;
