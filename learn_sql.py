import sqlite3
conn=sqlite3.connect("learn_sql.db")
cursor=conn.cursor()
cursor.execute("drop table if exists table1 ")
cursor.execute("CREATE TABLE if not exists TABLE1 (id integer primary key AUTOINCREMENT,name TEXT NOT NULL, age INTEGER check (age>0), gpa REAL DEFAULT 0.0 check (gpa>0 and gpa<=4))")
cursor.execute("INSERT INTO TABLE1 (name,gpa) VALUES(?,?)",("medhat",1.9))
students2_data = {
    "name": [
        "Ahmed", "Sara", "Omar", "Mona", "Youssef",
        "Nour", "Khaled", "Salma", "Tarek", "Hana",
        "Ziad", "Mariam", "Mostafa", "Aya", "Karim",
        "Farida", "Mahmoud", "Laila", "Hassan", "Nada"
    ],
    "age": [
        19, 20, 21, 18, 22,
        20, 19, 23, 21, 20,
        19, 22, 21, 18, 20,
        19, 20, 21, 22, 18
    ],
    "gpa": [
        3.45, 2.80, 3.92, 3.15, 2.15,
        3.60, 1.85, 4.00, 3.10, 2.50,
        2.40, 3.75, 2.95, 3.30, 1.90,
        3.88, 2.65, 3.50, 2.90, 3.70
    ]
}
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
rows1=list(zip(students2_data["name"],students2_data["age"],students2_data["gpa"]))


cursor.executemany("INSERT INTO TABLE1 (name,age,gpa) VALUES(?,?,?)",rows1)
cursor.execute("UPDATE TABLE1 SET gpa=? where name=?",(3.2,"Mahmoud"))
cursor.execute("DELETE FROM TABLE1 WHERE name=? ",("Nour",))
conn.commit()
cursor.execute("select gpa name from table1 where gpa>?",(3.9,))
cursor.execute("SELECT gpa,name from table1 order by gpa desc limit 3; ")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("select  count(*), max(gpa) ,avg(gpa) from table1")
ui=cursor.fetchone()
print(ui)
conn.close()
