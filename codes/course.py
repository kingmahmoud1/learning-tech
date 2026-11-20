import sqlite3
conn=sqlite3.connect("learn_sql.db")
cursor=conn.cursor()
cursor.execute("drop table if exists course")
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("create table  if not exists course (n_course integer primary key  AUTOINCREMENT,course_name text not null, id_student integer , result real default 0.0 check(result>=0 and result<=100),foreign key (id_student) references table1 (id) ON DELETE CASCADE,unique(course_name,id_student))")
courses_data = [
    ("Python", 95, 2),
    ("Discrete Math", 88, 2),
    ("Database", 91, 3),
    ("AI Fundamentals", 97, 4)
]
cursor.executemany("insert or ignore into course (course_name,result,id_student) values (?,?,?)",courses_data)
conn.commit()
cursor.execute("select table1.name,table1.gpa,course.course_name,course.result from table1 inner join course on table1.id=course.id_student")
for n in cursor.fetchall():
    print(n)
conn.close()
