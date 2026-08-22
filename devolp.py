import random 
while True :
    answer=input("if you want srart game entre 1 , to leave entre 0:\n")
    if answer=="1":
      input_number=""
      random_num=random.randint(0,9)
      str_random=str(random_num)
      while input_number!=str_random:
         input_number=input("Guss number , to leave entre 00:\n")
         print("you lose")
         if input_number=="00":
            break
         elif input_number==str_random:
            print("you win")
    elif answer=="0"     :
       break
    else:
       print("please choose between 0 or 1")
