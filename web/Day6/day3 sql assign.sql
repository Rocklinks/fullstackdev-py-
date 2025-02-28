create database students;
use students;

CREATE TABLE grades (
    student_id INT,
    student_name VARCHAR(50),
    subject VARCHAR(50),
    marks INT
);

INSERT INTO grades (student_id, student_name, subject, marks) VALUES
(1, 'Alice', 'Math', 85),
(2, 'Bob', 'Math', 92),
(3, 'Charlie', 'Math', 78),
(4, 'David', 'Science', 88),
(5, 'Eve', 'Science', 95),
(6, 'Frank', 'Science', 80),
(7, 'Grace', 'English', 90),
(8, 'Hank', 'English', 85),
(9, 'Ivy', 'English', 88);

SELECT 
    subject, 
    MAX(marks) AS highest_marks, 
    MIN(marks) AS lowest_marks
FROM grades
GROUP BY subject;

CREATE DATABASE SchoolDB;
USE SchoolDB;

-- Step 2: Create the students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

-- Step 3: Create the grades table
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject VARCHAR(50),
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Step 4: Insert sample data into students table
INSERT INTO students (student_id, student_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve'),
(6, 'Frank');

-- Step 5: Insert sample data into grades table (not all students have grades)
INSERT INTO grades (student_id, subject, marks) VALUES
(1, 'Math', 85),
(2, 'Math', 92),
(3, 'Science', 78),
(4, 'English', 88);

-- Step 6: Query to find students who have NOT received any grades
SELECT s.student_id, s.student_name
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
WHERE g.student_id IS NULL;

