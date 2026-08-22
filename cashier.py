products=["apple","milk","rice"]
price=(15,20,12)
cart_name=[]
cart_cost=[]

for i,u in  zip(products , price )  :
    print(f"we have {i} for {u} pound ")

while True :
   
    user=input("what do you want buy  and  write  recipe to see your items and leave write leave:\n" )
    use=user.lower()
    if use=="apple":
        vou=int(input(" how much do you want:\n"))
        much=vou*15
        cart_cost.append(much)
        cart_name.append("apple")
    elif use=="milk":
        vou2=int(input(" how much do you want:\n"))
        much2=vou2*20
        cart_cost.append(much2)
        cart_name.append("milk")
    elif use=="rice":
        vou3=int(input(" how much do you want:\n"))
        much3=vou3*12
        cart_cost.append(much3)
        cart_name.append("rice")
    elif use=="recipe":
        if len(cart_name)==0:
            print("your cart is empty")
        else :
         count=1
         for x,m in zip(cart_name,cart_cost) :
            print(f" {count}-you bought {x} with {m}")
            count+=1
         while True :
          finsh_answer=input("Do you want remove something or add or go to buy it:\n").lower()
          if finsh_answer=="remove":
            what=int(input("write tittle for this products:\n"))
            cart_cost.pop(what-1)
            cart_name.pop(what-1)
            for k,r in zip(cart_name,cart_cost):
                print(f"now your final cart is {k} with {r}")
          elif finsh_answer=="add":
             while True:
              what2=input("entre this product to leave write 0:\n")
             
              if what2=="apple":
                muc4=int(input("how mich do you want"))*15
                cart_name.append("apple")
                cart_cost.append(muc4)
                for m,f in zip(cart_name,cart_cost):
                 print(f"now your final cart is {m} with{f} ")
              elif what2=='0':
                 break


          elif finsh_answer=="buy":
             print("thank you for coming")
             break
            
          else :
             print("write correct")
    elif use=="leave":
        break
    else:
        print("we don't have this product")