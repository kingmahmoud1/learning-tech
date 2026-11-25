import sqlite3
file="task.db"
def connec():
  conn=sqlite3.connect("file")
  conn.row_factory=sqlite3.Row()
  conn.execute("pragma foreign_keys=on ;")
  return conn
def make_tb():
  with connec() as conn:
   conn.execute("create table if not exists task_tb (id integer primary key AUTOINCREMENT,title  unique not null,task  not null,task_done bool default 0 )")
   conn.execute("create table if not exists done_task (id_d integer primary key autoincerment,id_connect integer, foreign key (id_connect)  references task_tb (id) on delete cascade)")
  conn.close()
def add_data(title:str,task:str):
   try:
     with connec() as conn:
      conn.execute("insert into task_tb (title,task) values(?,?)on conflict (title) do update set task=excluded.task",(title,task))
     
     conn.close()
     return True 
   except sqlite3.Error as e :
      print(f"database error : {e}")
def all_tasks():
    conn=connec()
    
    cursor=conn.execute("select * from task_tb where task_done=?  ",(False,))
    rows=[dict(row) for row in cursor.fetchall()]
    return rows

def one_task(id:int):
    conn=connec()

    cursor=conn.execute("select * from task_tb where  id=? and task_done=? ",(id,False))
    row= cursor.fetchone()
    return dict(row) if row else None
    
def delete1(id:int):
    with connec() as conn:
        cursor= conn.execute("delete from task_tb where id=?",(id,))
        deleted=cursor.rowcount>0
    conn.close()
    return deleted
def d_task(id:int):
    try:
       with connec() as conn:
                cursor=conn.execute("update task_tb set task_done=? where id=?",(True,id))
                if cursor.rowcount==0:
                   conn.close()
                   return False
                conn.execute("insert into done_task (id_connect) values (?)",(id,))
                conn.close()
                return True
    except sqlite3.Error as e :
       print(f"database error :{e}")   
       return False
    
    
def show_d():
    conn=connec()
    
    cursor=conn.execute("select task_tb.title,task_tb.task,done_task.id_connect from task_tb inner join done_task on task_tb.id=done_task.id_connect")
    rows=[dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows
    


def upd(id:int,task:str):
   with connec() as conn:
    
    cursor=conn.execute("update task_tb set task=? where id=?",(id,task))
    update=cursor.rowcount>0
    conn.close()
    return update

