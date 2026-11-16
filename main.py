from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class Book_c(BaseModel):
    name:str
    id:int
    is_exist:bool=True
    
class Book_r(BaseModel):
        name:str
        id:int
        
book_li=[]
@app.post("/add_book")
def add(book:Book_c):
    book_li.append(book.model_dump())

@app.get("/book_menu/{name1}",response_model=Book_r)
def work(name1:str):
   
    for i in book_li :
        
        if i["name"]==name1:
           
            return i
    else :
        raise HTTPException(status_code=404,
                            detail="we can't find this book")
@app.put("/change")
def work2(book2:Book_c,name2:str):
    for index , y in enumerate(book_li):
       if y["name"]==name2:
         book_li[index]=book2.model_dump()
         return {"message":"you adit the data succesfully"}
    else:
        raise HTTPException(status_code=404,
                            detail="we can't find this book")
@app.delete("/delelte")
def work3(name3:str):
    for  index1,z in enumerate (book_li ):
        if z["name"]==name3:
            book_li.pop(index1)
            return {"message":"ok"}

    raise HTTPException(status_code=404,
                          detail="we can't find this book")