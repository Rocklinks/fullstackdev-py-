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
