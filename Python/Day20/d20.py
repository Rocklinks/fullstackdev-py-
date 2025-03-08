 import mysql.connector
 conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="1111"
 )
 cursor = conn.cursor()
 cursor.execute("CREATE DATABASE IF NOT EXISTS COMPANY")
 conn.commit()

 cursor.execute("USE COMPANY")
 cursor.execute("""
     CREATE TABLE IF NOT EXISTS employees (
         id INTEGER PRIMARY KEY AUTO_INCREMENT,
         name TEXT,
         department TEXT,
         salary REAL
     )
 """)
 conn.commit()

 cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Raja Ganesh', 'FrontEnd', 40000.0)")
 cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Shiva Kumar', 'Marketing', 50000.0)")
 cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Gideon Abraham', 'BDE', 70000.0)")
 conn.commit()

 cursor.execute("SELECT * FROM employees")
 for employee in cursor.fetchall():
     print(employee)


 cursor.execute("UPDATE employees SET salary = 45000.0 WHERE name = 'Raja Ganesh'")
 conn.commit()


 cursor.execute("SELECT * FROM employees WHERE name = 'Raja Ganesh'")
 #updated_employee = cursor.fetchone()
 print(f"Updated Employee: {cursor.fetchone()}")

 cursor.execute("DELETE FROM employees WHERE name = 'Shiva Kumar'")
 conn.commit()

 cursor.execute("SELECT * FROM employees")
 print(f"Remaining Employees: {cursor.fetchall()}")

cursor.close()
conn.close()

import re
def contacts(text):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    phone_pattern = r"\b\d{10}\b|\b\d{3}-\d{3}-\d{4}\b"

    email = re.findall(email_pattern,text)
    phone = re.findall(phone_pattern, text)
    return email, phone

text = input("Enter a para of text: ")
email,phone =contacts(text)
print(f"Extracted Emails: {email}")
print(f"Extracted numbers: {phone}")
