CREATE TABLE `Products`(
    `Code` INT UNSIGNED NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Entry Date` DATE NOT NULL,
    `Brand` VARCHAR(255) NOT NULL,
    `Stock available` INT NOT NULL,
    PRIMARY KEY(`Code`)
);
CREATE TABLE `Invoices`(
    `Invoice Number` INT UNSIGNED NOT NULL,
    `Purchase date` DATE NOT NULL,
    `Buyer email` VARCHAR(255) NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    PRIMARY KEY(`Invoice Number`)
);
CREATE TABLE `Products Per Invoice`(
    `Quantity` INT UNSIGNED NOT NULL,
    `Total amount` DECIMAL(8, 2) NOT NULL,
    `Invoice Number` INT NOT NULL,
    `Product Code` INT NOT NULL,
    PRIMARY KEY(`Invoice Number`)
);
ALTER TABLE
    `Products Per Invoice` ADD PRIMARY KEY(`Product Code`);
CREATE TABLE `Shopping Cart`(
    `Buyer email` VARCHAR(255) NOT NULL,
    `Products` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`Products`)
);
CREATE TABLE `Products Per Shopping Cart`(
    `Products` VARCHAR(255) NOT NULL,
    `Product Code` INT NOT NULL,
    PRIMARY KEY(`Products`)
);
ALTER TABLE
    `Products Per Shopping Cart` ADD PRIMARY KEY(`Product Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Shopping Cart` ADD CONSTRAINT `products per shopping cart_product code_foreign` FOREIGN KEY(`Product Code`) REFERENCES `Products`(`Code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice number_foreign` FOREIGN KEY(`Invoice Number`) REFERENCES `Invoices`(`Invoice Number`);
ALTER TABLE
    `Products Per Shopping Cart` ADD CONSTRAINT `products per shopping cart_products_foreign` FOREIGN KEY(`Products`) REFERENCES `Shopping Cart`(`Products`);