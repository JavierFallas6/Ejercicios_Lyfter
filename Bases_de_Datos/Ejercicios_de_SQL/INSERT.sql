INSERT INTO Products (Name, Price, Entry_Date, Brand, Stock_available)
VALUES
('Laptop', 450000.00, '2026-10-01', 'Dell', 10),
('Mouse', 8500.00, '2026-10-02', 'Logitech', 25),
('Keyboard', 15000.00, '2026-10-03', 'Logitech', 15);


INSERT INTO Invoice (Invoice_Number, Purchase_Date, Buyer_email, Total_amount,Buyers_phone, Employee_Code)
VALUES
(1, '2026-10-10', 'juan@gmail.com', 458500.00, '8856-2563',1),
(2, '2026-10-11', 'juan@gmail.com', 15000.00,'8856-2565',2),
(3, '2026-10-12', 'maria@gmail.com', 8500.00,'8856-2564',1);


INSERT INTO Shopping_Cart (Buyer_email, Products)
VALUES
('juan@gmail.com', 'Laptop'),
('maria@gmail.com', 'Mouse');


INSERT INTO Products_Per_Invoice (Quantity, Total_amount, Invoice_Number_id, Product_Code_id)
VALUES
(1, 450000.00, 1, 1),
(1, 8500.00, 1, 2),
(1, 15000.00, 2, 3),
(1, 8500.00, 3, 2);


INSERT INTO Products_Per_Shopping_Cart (Shopping_cart_id, Product_Code_id)
VALUES
(1, 1),
(2, 2);


