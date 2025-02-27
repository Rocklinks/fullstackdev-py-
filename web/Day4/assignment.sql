-- create database if not exists student_management;
-- use student_management;
-- create table if not exists students (
-- student_id INT Primary Key AUTO_INCREMENT,
-- name VARCHAR(50) NOT NULL,
-- age INT CHECK (age > 0),
-- email VARCHAR(100) UNIQUE
-- );

-- insert into students (name ,age,email)
-- values 
-- ("John" ,28,"johnbritto@gmail.com"),
-- ("Santhosh" ,26,"santhosh26@gmail.com"),
-- ("Nivin" ,26,"nivin25@gmail.com"),
-- ("Nirinjan" ,29,"nirinjan@gmail.com"),
-- ("Raja" ,31,"raja1993@gmail.com");

-- select * from students;

create database if not exists enrollment;
use enrollment;

create table if not exists courses(course_id int primary key auto_increment,
					course_name varchar(100) not null,
                    duration int not null
                    );
create table if not exists enrollments (
					enrollment_id int primary key auto_increment,
                    student_id int not null,
                    course_id int not null,
                    foreign key(course_id) references courses
);

insert into courses (course_name, duration) values
('python Programming',10),
('Web Development',12),
('Data Science',16);

insert into enrollments(student_id,course_id) values
(102,1),
(103,2),
(104,3),
(105,2),
(106,1);

select * from enrollments;

SELECT e.student_id, c.course_name 
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Python Programming';




