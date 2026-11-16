#--------------------بسم الله الرحمن الرحيم------------------------------
#--------------------مكتبة----------------------------------------------
system=[]
earning=[]
def add():
    name1=input("what is the book name:\n").lower()
    while True:
        try:
          quantity=int(input("how many books we do get:\n"))
          break
        except:
           print("we need number")
    while True:
       try:
         cost=float(input("what price for one book:\n "))
         break
       except:
          print("we need number")
    book_data={"name":name1,"amount":quantity,"price":cost}
    system.append(book_data)
def sell():
   check=input("what name for this book :\n").lower()
   found1=False
   for i in system:
      if i["name"]==check:
         found1=True
         while True:
            try:
               sell=int(input("how many book do you sell"))
               break
            except:
               print("write number")
         i["amount"]=i["amount"]-sell
         earnings=sell*i["price"]
         earning.append([earnings,i["name"]])
         earning.sort(reserve=True)
      if not found1:
         print("we can't find this book")
def show():
   if len(system)!=0:
    for loi in system:
       print(loi)
    else :
       print("we don't have enogh data")
def edit():
   check2=input("what this book name:\n").lower()
   for uio in system:
      found2=False
      if uio["name"]==check2:
         found2=True
         while True :
            try :
               new_cost=int(input("what the new price\n"))
               break
            except:
               print("wrong inputs")
         uio["price"]=new_cost
      if not found2:
         print("we can't find this book")
def search():
   name3=input("what the book name:\n").lower()
   found5=False
   for jkl in system:
      if jkl["name"]==name3:
         found5=True
         print(jkl)
#--------------------التشغيل--------------------------------
print(" add book 1 , sell 2 , show data 3 , edit price 4, search 5 , leave 6")
menu=input("write 1 : 6 \n")
while True :
   if menu=="1":
      add()
   elif menu=="2":
      sell()
   elif menu=="3":
      show()
   elif menu=="4":
      edit()
   elif menu=="5":
      search()
   elif menu=="6":
      break
   else:
      print("entre from 1 to 6")