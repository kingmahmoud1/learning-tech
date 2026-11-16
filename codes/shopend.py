from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
app=FastAPI()

class product_add(BaseModel):
    name:str
    amount:int
    type:str

class product_show(BaseModel):
    name:str
    type:str

products_list=[]

@app.post("/add/new_product")
def add(product:product_add):
    products_list.append(product.model_dump())

@app.get("/",response_model=list[product_show])
def show_all():
    if len(products_list)!=0:
    
        return products_list
    else:
        raise HTTPException(status_code=404,
                                   detail="no_data")
@app.get("/{name1}",response_model=product_show)
def show_one(name1:str):
   for j in products_list:
      if j["name"]==name1:
         return j
   raise HTTPException(status_code=404,
                                     detail="no_data")
@app.put("/buy/{name2}")
def buy(name2:str):
   for index,acc in enumerate(products_list):
      if acc["name"]==name2 and acc["amount"]>0:
         products_list[index]["amount"]= products_list[index]["amount"]-1
         return
   raise HTTPException(status_code=404,
                                         detail="no_data")
@app.delete("/delete/{name3}")
def delelte(name3:str):
   for index2, z in enumerate(products_list):
      if z["name"]==name3:
         products_list.pop(index2)
         return
   raise HTTPException(status_code=404,
                                             detail="no_data")

      