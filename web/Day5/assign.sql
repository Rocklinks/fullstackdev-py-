create database if not exists company;
use company;

create table if not exists employees(
					id int primary key auto_increment,
                    name varchar(60),
                    age int,
                    department varchar(10),
                    salary float(10)
);

insert into employees(name, age,department,salary) values
	('Saravana',26,"Backend ",25000),
	('Muthu',29,"Backend ",30000),
	('Ravi teja',35,"Frontend ",40000),
	('Siddharth',30,"Fullstack ",31000);