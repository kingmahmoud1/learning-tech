import sqlite3
conn=sqlite3.connect("pro.db")
cursor=conn.cursor()
cursor.execute("pragma foreign_keys=on ;")
cursor.execute(" create table if not exists inf (id_t integer primary key autoincrement ,name_t text not null unique ,level_t text not null check(lower(level_t) in ('junior','senior','ecpc')),uni_n text default 'cairo')  ")

cursor.execute("create table if not exists sub  (id_s integer primary key autoincrement,sub_n text not null,id_te integer,result integer default 0.0 check(result>=0 and result<=100),attemp integer check(attemp>=1) ,foreign key (id_te)  references inf (id_t) on delete cascade, unique(id_te,sub_n))")
teams_data = [
    ("PyKnights", "junior", "Cairo University"),
    ("Binary beasts", "senior", "Cairo University"),
    ("SegFault Squad", "ecpc", "Cairo University"),
    ("Code Pharaohs", "junior", "Ain Shams University"),
    ("NullPointers", "senior", "Cairo University")  
]
submissions_data = [
    (1, "A", 100, 1),
    (1, "B", 85, 3),
    (2, "A", 100, 1),
    (2, "B", 100, 2),
    (2, "C", 70, 4),
    (3, "A", 100, 1),
    (3, "C", 95, 2),
    (4, "A", 60, 2)
]
cursor.executemany("insert or ignore into inf (name_t,level_t,uni_n)values(?,?,?) ",teams_data)
cursor.executemany("insert or ignore into sub(id_te,sub_n,result,attemp)values(?,?,?,?)",submissions_data)
value=("Binary beasts","ecpc")
cursor.execute("insert into inf (name_t,level_t) values(?,?)on conflict (name_t) do update set level_t=excluded.level_t",value)
wrong_data=[ (4, "B", 150, 1), (99, "A", 90, 1)]
for i in wrong_data:
    try:
        cursor.execute("insert into sub (id_te,sub_n,result,attemp)values(?,?,?,?)",i)
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(e)
        conn.rollback()
conn.commit()
score_board="""
select inf.id_t,inf.name_t , count(sub.id_s) as solved_sub ,COALESCE(sum(sub.result),0) as total_points 
from inf left join sub on inf.id_t=sub.id_te 
group by inf.id_t
ordered by total_points desc
"""
cursor.execute(score_board)
for n in cursor.fetchall():
    print(n)
here_we_go="""
select inf.uni_n,count(sub.result),sum(sub.attemp)
from inf inner join sub on inf.id_t=sub.id_t
where sub.result>=80 
group by inf.uni_n
having count(sub.result)>=2
ordered by count(sub.result) desc
"""
conn.close()