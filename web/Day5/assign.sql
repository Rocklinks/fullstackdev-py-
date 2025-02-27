-- create database if not exists company;
-- use company;

-- create table if not exists employees(
-- 					id int primary key auto_increment,
--                     name varchar(60),
--                     age int,
--                     department varchar(10),
--                     salary float(10)
-- );

-- insert into employees(name, age,department,salary) values
-- 	('Saravana',26,"Backend ",55000),
-- 	('Muthu',29,"Backend ",64000),
-- 	('Ravi teja',35,"Frontend ",45000),
-- 	('Siddharth',30,"Fullstack ",48000);
--     
--     
-- select * from employees where salary > 50000;
--     
-- select * from employees order by salary desc;

-- create database if not exists record_management;
-- use record_management;

-- create table if not exists students(
-- 					id int primary key auto_increment,
--                     name varchar(50) not null,
--                     age int not null,
--                     grade varchar(2) not null
-- );

-- insert into students(name,age,grade) values
-- 					('Saran',12,"A"),
-- 					('Siva',15,"B"),
-- 					('Sakthi',19,"C");

-- UPDATE students
-- SET grade='A'
-- WHERE grade='O';

-- select * from students;

-- SET SQL_SAFE_UPDATES = 0;
-- delete from students
-- where age>12;

-- select * from students;

create database if not exists advanced;
use advanced;

create table if not exists customers(
							customer_id int primary key auto_increment,
                            customer_name varchar(70) not null,
                            city varchar(30) not null,
                            membership_type varchar(30) not null
);

insert into customers(customer_name,city,membership_type) values
 ('Shashvanth','Armenia','Permanent'),
 ('Abishek','Los Angeles','Permanent'),
 ('Armen','New York','30 Days Trial'),
 ('Shrikanth','New York','30 Days Trial');
 
select * from customers;
 
select * from customers
where customer_name Like 'A%';
 
select * from customers
where  city in ('New York','Los Angeles');































    
    