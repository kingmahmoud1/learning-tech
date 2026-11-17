import sqlite3
conn=sqlite3.connect("learn_sql.db")
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS TABLE1 (name TEXT, age INTEGER, gpa REAL DEFAULT 0.0)")
cursor.execute("INSERT INTO TABLE1 (name,gpa) VALUES(?,?)",("medhat",8.9))

students_data = {
    "name": [
        "Ahmed", "Sara", None, "Omar", "Mona",
        "Youssef", "Nour", "Khaled", None, "Salma",
        "Tarek", "Hana", "Ziad", "Mariam", None,
        "Mostafa", "Aya", "Karim", "Farida", "Mahmoud"
    ],
    "age": [
        19, -20, 21, None, 18,
        -5, 22, 20, 19, None,
        23, -18, 21, 20, 19,
        None, 22, -21, 18, 20
    ],
    "gpa": [
        3.45, 2.80, None, 3.92, -1.5,
        2.15, 3.60, None, 1.85, 4.00,
        3.10, 2.50, -0.4, 3.75, 2.95,
        3.30, None, 1.90, 3.88, 2.65
    ]
}
rows1=list(zip(students_data["name"],students_data["age"],students_data["gpa"]))


cursor.executemany("INSERT INTO TABLE1 (name,gpa,age) VALUES(?,?,?)",rows1)
cursor.execute("UPDATE TABLE1 SET gpa=? where name=?",(9,"Mahmoud"))
cursor.execute("DELETE FROM TABLE1 WHERE name=? ",("Nour",))
conn.commit()
cursor.execute("SELECT age,gpa,name from table1 where gpa>? ",(2,))
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()
