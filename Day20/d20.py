# import mysql.connector
# conn = mysql.connector.connect(
# host="localhost",
# user="root",
# password="1111"
# )
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS COMPANY")
# conn.commit()

# cursor.execute("USE COMPANY")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY AUTO_INCREMENT,
#         name TEXT,
#         department TEXT,
#         salary REAL
#     )
# """)
# conn.commit()

# cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Raja Ganesh', 'FrontEnd', 40000.0)")
# cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Shiva Kumar', 'Marketing', 50000.0)")
# cursor.execute("INSERT INTO employees (name, department, salary) VALUES ('Gideon Abraham', 'BDE', 70000.0)")
# conn.commit()

# cursor.execute("SELECT * FROM employees")
# for employee in cursor.fetchall():
#     print(employee)


# cursor.execute("UPDATE employees SET salary = 45000.0 WHERE name = 'Raja Ganesh'")
# conn.commit()


# cursor.execute("SELECT * FROM employees WHERE name = 'Raja Ganesh'")
# #updated_employee = cursor.fetchone()
# print(f"Updated Employee: {cursor.fetchone()}")

# cursor.execute("DELETE FROM employees WHERE name = 'Shiva Kumar'")
# conn.commit()

# cursor.execute("SELECT * FROM employees")
# print(f"Remaining Employees: {cursor.fetchall()}")

import re

