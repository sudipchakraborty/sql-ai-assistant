import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

employees = [
    ("Rahul", "IT", 80000, 5),
    ("Anita", "HR", 60000, 3),
    ("Vikram", "Sales", 90000, 7),
    ("Sneha", "Finance", 75000, 4),
    ("Arjun", "IT", 95000, 8)
]

cursor.executemany("""
INSERT INTO employees (
    employee_name,
    department,
    salary,
    experience
)
VALUES (?, ?, ?, ?)
""", employees)

conn.commit()

conn.close()

print("Database created successfully!")