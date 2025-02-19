
##Task1
import re
def contacts(text):
    pattern = r"\b[Pp]\w+"

    p = re.findall(pattern, text)
    return p

text = input("Enter a sentences of text: ")
p =contacts(text)
print(f"P Pattern: {p}")

#Task2
import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="1111"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS SCHOOL")
conn.commit()

cursor.execute("USE SCHOOL")
cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTO_INCREMENT,
#         name TEXT,
#         marks INT
#     )
# """)
conn.commit()

cursor.execute("INSERT INTO employees (name, marks) VALUES ('Sathish', 40)")
cursor.execute("INSERT INTO employees (name, marks) VALUES ('Santhosh', '50)")
cursor.execute("INSERT INTO employees (name, marks) VALUES ('Abraham', 70)")
conn.commit()

cursor.execute("SELECT * FROM students")
for student in cursor.fetchall():
    print(student)


#Task3
cursor.execute("use COMPANY")
dept_name = input("Enter department name: ")
query = "SELECT * FROM employees WHERE department = %s"
cursor.execute(query, (dept_name,))

employees = cursor.fetchall()
if employees:
    print(f"Employees in {dept_name} department:")
    for emp in employees:
        print(emp)
else:
    print(f"No employees found in {dept_name} department.")

cursor.close()
conn.close()