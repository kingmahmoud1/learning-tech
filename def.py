school_date=[]
import json
def lood_data():
   global school_date
   try:
     with open("school.json","r")as file:
      school_date=json.load(file)
   except FileNotFoundError:
      school_date=[]
def save_data():
   with open("school.json","w")as file:
      json.dump(school_date,file,indent=4)

def add():
    name=input("what is his name:\n").lower()
    while True:
     try:
      age=int(input("how old is he :\n"))
      break
     except:
        print("please write numbers")
    
    while True :
       try:
        score=input("How score does he get in the first exam:\n")
        scor=float(score.replace("%",""))
        break
       except:
          print("write numbers")
    student_data={"name":name, "age":age, "result":[scor]}
    school_date.append(student_data)
    save_data()
def show():
    if len(school_date)==0:
       print("no data available")
    else: 
      for i in school_date:
        print(i)
def edit():
   named=input("who this student:\n")
   lo=False
   for a in school_date:
      if a["name"]==named:
         lo=True
         while True:
            try:
             age2=int(input("Jow old are you now :\n"))
             break
            except:
               print("write number")
         a["age"]=age2
   if not lo:
       print("this is incorrect data")
   save_data()
def exames():
   who=input("who is this student:\n")
   ji=False
   for lk in school_date:
      if lk["name"]==who:
         ji=True
         while True:
          an = input(" add scores 1 , leave 2")
          if an=="1":
              
              while True:
                try:
                  score2=input("How score does he get:\n")
                  score3=float(score2.replace("%",""))
                  break
                except:
                   print("write number")
              lk["result"].append(score3)
          elif an=="2":
               break 
   if not ji:
        print("it's incorrect data")
   save_data()
def top():
   top_list=[]
   for mon in school_date:
     total=sum(mon["result"])
     top_list.append([total,mon["name"]])
   top_list.sort(reverse=True)
   print("------- ranking school------")
   for index, students in enumerate(top_list,start=1):
      print(f" rank {index} is {students[1]} with total score:{students[0]}")
def remove():
   num5=input("what is he name:\n")
   found=False
   for tol in school_date :
      if tol["name"]==num5:
         school_date.remove(tol)
         found=True
         break
   if not found :
         print("wrong data")
   save_data()
#---------------التشغيل-----------------------
lood_data()
while True :
   print("---add 1 , edit age 2 , show students 3 , ranking 4 , remove 5 ,add exames 6, leave 7")
   menu= input("entre 1:7:\n")
   if menu=="1":
      add()
   elif menu=="2":
      edit()
   elif menu=="3":
      show()
   elif menu=="4":
      top()
   elif menu=="5":
      remove()
   elif menu=="6":
      exames()
   elif menu=="7":
      break
   else:
      print("wrong input")
