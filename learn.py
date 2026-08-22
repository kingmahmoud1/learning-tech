import random 
while True :
    answer=input("if you want srart game entre 1 , to leave entre 0:\n")
    if answer=="1":
      input_number=""
      random_num=random.randint(0,9)
      str_random=str(random_num)
      for i in range(1,4):
         ko=input("Guss number , to leave entre00:\n")
         if ko==str_random or ko=="00":
            print("hard luck")
            break
    elif answer=="0"     :
       break
    else:
       print("please choose between 0 or 1")
