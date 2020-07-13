
-- Create Database 
CREATE DATABASE GroceryGo;

USE GroceryGo;

-- User table
CREATE TABLE IF NOT EXISTS users (
    UserID INT(11) AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255),
    UserName VARCHAR(200),
    Password LONGTEXT ,
    Email VARCHAR(50),
    Gender varchar(50) ,
	DateofBirth DATE,
	PhoneNumber varchar(50)
)  ENGINE=INNODB;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    ProductID INT(11) AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    SubCategory VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    Image varchar(255),
    Price FLOAT,
    Discount Int(3)
)  ENGINE=INNODB;

-- orders table
-- CREATE TABLE IF NOT EXISTS orders (
--     OrderID INT(11) AUTO_INCREMENT PRIMARY KEY,
--     UserID INT(11) ,
--     FOREIGN KEY (UserID) REFERENCES users(UserID)
-- )  ENGINE=INNODB;

-- CREATE TABLE IF NOT EXISTS orderItemMap (
--     OrderItemID INT(11) AUTO_INCREMENT PRIMARY KEY,
--     UserID INT(11) ,
--     ProductID INT(11) ,
--     FOREIGN KEY (UserID) REFERENCES users(UserID),
--     FOREIGN KEY (ProductID) REFERENCES products(ProductID)
-- )  ENGINE=INNODB;

-- DELETE script test
DELETE FROM products WHERE ProductID=1;
-- delete from users;
-- select * from users;

-- set foreign_key_checks=0;
-- truncate table users;
-- set foreign_key_checks=1;

SELECT * FROM products;
INSERT INTO products VALUES (1,'Nestle','Dairy','Milk','500Ml','',1.5,0);
INSERT INTO products VALUES (2,'Lidl','Dairy','Milk','500Ml','',1.5,0);
INSERT INTO products VALUES (3,'Banana','Fresh','Fruits','5 Pieces','https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80',1.29,0);
INSERT INTO products VALUES (4,'Banana','Fresh','Fruits','10 Pieces','https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80',1.29,0);
INSERT INTO products VALUES (5,'Aldi','Dairy','Milk','500Ml','https://images.unsplash.com/photo-1550583724-b2692b85b150?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',2,0);
INSERT INTO products VALUES (6,'Nestle','Dairy','Milk','500Ml','',1.5,0);
INSERT INTO products VALUES (7,'Lidl','Dairy','Milk','500Ml','',1.5,0);
INSERT INTO products VALUES (8,'Banana','Fresh','Fruits','5 Pieces','https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80',1.29,0);
INSERT INTO products VALUES (9,'Banana','Fresh','Fruits','10 Pieces','https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80',1.29,0);
INSERT INTO products VALUES (10,'Aldi','Dairy','Milk','500Ml','https://images.unsplash.com/photo-1550583724-b2692b85b150?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',2,0);

-- update test
UPDATE products
SET
    Image = 'https://images.unsplash.com/photo-1557800636-894a64c1696f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2801&q=80'
WHERE
    ProductID = 11;

 -- added wallet column
ALTER TABLE users
ADD COLUMN Wallet VARCHAR(20) ;

 -- added ordered products column
ALTER TABLE users
ADD COLUMN OrderedProducts longtext;

-- ALTER TABLE users CHANGE orderedProducts OrderedProducts longtext;

--  -- added order details column
-- ALTER TABLE orders
-- ADD COLUMN ProductId Int(11),ADD COLUMN NumberOfItems Int(11) ;

-- Select * from users;

-- SELECT * FROM products where ProductID=1
-- UPDATE users SET Wallet = '50' ;
