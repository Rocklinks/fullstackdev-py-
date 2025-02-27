create database if not exists db;
use db;

CREATE TABLE if not exists users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100), 
    bio TEXT   
);
CREATE TABLE if not exists customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    cname VARCHAR(100) NOT NULL
);

CREATE TABLE if not exists orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,  -- Foreign Key linking to customers
    order_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);
INSERT INTO customers (cname) VALUES ('Alice'), ('Bob');

INSERT INTO orders (customer_id, order_date, amount) 
VALUES (1, '2024-02-27', 250.00),
       (1, '2024-02-28', 100.00),
       (2, '2024-02-27', 75.00);


select * from users;
select * from customers;
select * from orders;