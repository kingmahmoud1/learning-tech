tasks=[]
while True:
 while True :
    options=input("add task 1 , see your tasks 2 , exit 3 :\n")
    if options=="1":
        add=input("write your task:\n")
        tasks.append(add)
    elif options=="2":
        for i in tasks:
           print(f"your tasks is {i}")
        answer=input("if you want remove task write remove:\n")
        answe=answer.lower()
        if answe=="remove":
            reply=int(input("choose the endix for this task:\n"))
            tasks.pop(reply-1)
        else:
            print("this is your task")
    elif options=="3":
        break
    else: 
       print ("choose between 1 , 2, 3 ")