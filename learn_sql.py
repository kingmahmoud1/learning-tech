import sqlite3
conn=sqlite3.connect("learn_sql.db")
cursor=conn.cursor()
cursor.execute("drop table if exists table1 ")
cursor.execute("CREATE TABLE if not exists TABLE1 (id integer primary key AUTOINCREMENT,name TEXT NOT NULL, age INTEGER check (age>0), gpa REAL DEFAULT 0.0 check (gpa>=0 and gpa<=4),user_name text unique not null , partion text check(lower(partion) in ('ai','cs','it')))")

students2_data = {
    "name": [
        "Mahmoud", "Ahmed", "Salma", "Omar", "Mona",
        "Youssef", "Sara", "Ali", "Nour", "Kareem",
        "Hala", "Mostafa", "Aya", "Tarek", "Mariam",
        "Ziad", "Menna", "Hassan", "Farah", "Ibrahim"
    ],
    "age": [
        18, 19, 20, 21, 18,
        22, 19, 20, 21, 19,
        18, 23, 20, 22, 19,
        18, 21, 20, 19, 22
    ],
    "gpa": [
        3.85, 3.40, 3.92, 2.75, 3.10,
        2.50, 3.65, 3.20, 3.98, 2.90,
        3.55, 2.15, 3.70, 3.05, 3.80,
        0.00, 3.30, 2.85, 3.60, 3.45
    ],
    "user_name": [
        "mahmoud_01", "ahmed_02", "salma_03", "omar_04", "mona_05",
        "youssef_06", "sara_07", "ali_08", "nour_09", "kareem_10",
        "hala_11", "mostafa_12", "aya_13", "tarek_14", "mariam_15",
        "ziad_16", "menna_17", "hassan_18", "farah_19", "ibrahim_20"
    ],
    "partion": [
        "ai", "cs", "ai", "it", "cs",
        "it", "ai", "cs", "ai", "it",
        "cs", "it", "ai", "cs", "ai",
        "cs", "it", "cs", "ai", "it"
    ]
}

rows1=list(zip(students2_data["name"],students2_data["age"],students2_data["gpa"],students2_data["user_name"],students2_data["partion"]))


cursor.executemany("INSERT INTO TABLE1 (name,age,gpa,user_name,partion) VALUES(?,?,?,?,?)",rows1)
cursor.execute("insert into table1 (name,user_name,gpa) values(?,?,?) on conflict(user_name) do update set gpa=excluded.gpa ",("Mahmoud","mahmoud_01",4))
cursor.execute("UPDATE TABLE1 SET gpa=? where name=?",(3.2,"Menna"))
cursor.execute("DELETE FROM TABLE1 WHERE name=? ",("Nour",))
conn.commit()
cursor.execute("select gpa name from table1 where gpa>?",(3.9,))
cursor.execute("SELECT gpa,name from table1 order by gpa desc limit 3; ")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.execute("select  count(*), max(gpa) ,round(avg(gpa),2) from table1")
ui=cursor.fetchone()
print(ui)
cursor.execute("select partion , count(*),max(gpa),round(avg(gpa),2) from table1 group by partion ")
r=cursor.fetchall()
for j in r:
    print(j)
cursor.execute("select name ,gpa from table1 order by gpa desc limit 3; group by partion")
c=cursor.fetchall()
for l in c :
    print(l)
conn.close()
