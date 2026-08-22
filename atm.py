password="299888"
while True:
 balance=1000

 for i in range(0,3):
    use_pass=input("entre the password")
    if use_pass==password:
        while True:
            options=input("1 add mony , 2 take mony , 3 exi:t\n")
            if options=="1":
        
                add=float(input("entre the money:\n"))
                balance+=add
                print(f"now ,your balance is{balance} ")
            elif options=="2":
                mins=float(input("how much money do you want:\n"))
                if balance>=mins :
                  balance-=mins
                  print(f"yourfinal balnce is {balance}")
                else:
                    print("you don't have enogh")
            elif options=="3":
                break
            else:
                print("choose between 1 or 2 or 3 ")
        break
    else:
        print("this password is incorrect")
