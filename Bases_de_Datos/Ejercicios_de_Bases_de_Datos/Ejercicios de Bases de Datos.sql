CREATE TABLE `Products`(
    `Code` INT UNSIGNED NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` FLOAT(53) NOT NULL,
    `Entry Date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice Number` INT UNSIGNED NOT NULL,
    `Purchase date` DATE NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` FLOAT(53) NOT NULL,
    PRIMARY KEY(`Invoice Number`)
);
ALTER TABLE
    `Invoices` ADD PRIMARY KEY(`Buyer email`);
CREATE TABLE `Products Per Invoice`(
    `Quantity` INT UNSIGNED NOT NULL,
    `Total amount` FLOAT(53) NOT NULL,
    `Invoice Number` INT NOT NULL,
    `Product Code` INT NOT NULL,
    PRIMARY KEY(`Invoice Number`)
);
ALTER TABLE
    `Products Per Invoice` ADD PRIMARY KEY(`Product Code`);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Products` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Buyer email`)
);
ALTER TABLE
    `Invoices` ADD CONSTRAINT `invoices_buyer email_foreign` FOREIGN KEY(`Buyer email`) REFERENCES `Shopping Cart`(`Buyer email`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Shopping Cart` ADD CONSTRAINT `shopping cart_products_foreign` FOREIGN KEY(`Products`) REFERENCES `Products`(`Code`);