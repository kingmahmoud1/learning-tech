import sqlite3
conn=sqlite3.connect("learn_sql.db")
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS TABLE1 (name TEXT, age INTEGER, gpa REAL DEFAULT 0.0)")
cursor.execute("INSERT INTO TABLE1 (name,gpa) VALUES(?,?)",("mahmoud",8.9))
raw_list={"name":["mahmoud","ALi","mona","salma","mahmoud"],
          "age":[21,-12,None,32,21],
            "gpa":[86,25,28,29,9]}

rows1=list(zip(raw_list["name"],raw_list["age"],raw_list["gpa"]))
value=[("mah",9),("mona",8)]
cursor.executemany("INSERT INTO TABLE1 (name,gpa) VALUES(?,?)",value)
cursor.executemany("INSERT INTO TABLE1 (name,gpa,age) VALUES(?,?,?)",rows1)
cursor.execute("UPDATE TABLE1 SET gpa=? where name=?",(9,"mahmoud"))
cursor.execute("DELETE FROM TABLE1 WHERE name=? ",("mahmoud",))
conn.commit()
cursor.execute("SELECT age,gpa,name from table1 where gpa>? ",(2,))
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()
