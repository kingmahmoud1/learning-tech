from fastapi import FastAPI , HTTPException
import sqlite3
from pydantic import BaseModel
class Inf(BaseModel):
   id:int
   price:int
   discount:int



app=FastAPI()
conn=sqlite3.connect("ch1.db")
cursor=conn.cursor()
@app.get("/homebage")
def g_a_work():
    cursor.execute("select order_id,price,discount from tb1")
    return cursor.fetchall()
        
@app.get("/{order_id}")
def g_work(order_id:int):
     
     try:
       cursor.execute("select order_id , price ,discount from tb1 where order_id=?",(order_id,))
       for n in cursor.fetchall():
               return n
     except:
        raise HTTPException(status_code=404,
                            detail="rrrrr")
@app.put("/{id}/{new}")
def p_work(id:int,new:int):
    try:
     cursor.execute("update tb1 set discount=? where order_id=?,"(new,id))
    except:
       raise HTTPException(status_code=404,
                            detail="we can't find this book")
@app.post("/new_order")
def a_work(inf:Inf):
   cursor.execute("insert into tb1 (order_id,price,discount) on conflict (order_id) set excluded.price=price values(?,?,?)",inf)
@app.delete("/delete/{id}")
def d_work(id:int):
    cursor.execute("delete from tb1 where order_id=?",(id,))

    
