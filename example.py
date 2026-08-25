class my_list:
    def __init__(self):
        self.food=[]
    def add(self,order):
        self.food.append(order)
    def len(self):
        return len(self.food)
    def is_empty(self):
        if len(self.food)==0:
            return True
        else:
            return False
class stack(my_list):
    # Lifo
    def __init__(self):
        super(). __init__()
    def pop(self):
        if not self.is_empty():
               return self.food.pop()
    def peak1(self):
        if not self.is_empty():
            return self.food[-1]
class queue(my_list):
    #FiFo
    def __init__(self):
        super().__init__()
    def dequeue(self):
        if not self.is_empty():
          return  self.food.pop(0)
    def peak2(self):
        if not self.is_empty():
            return self.food[0]
food1=stack()
food2=queue()
print("*******************************************")
print("*****This system for make the orders much eaiser *********************")
while True:
    print(" to add order 1 , show new order 2 , endo order 3 ")
    menu=input()
    if menu=="1":
        order1=input(" write your order")
        food2.add(order1)
    elif menu=="2":
        while True :
         print(f" there are {food2.len()} orders")
         print(" you have to finsh this order")
         print(food2.peak2())
         que=(input("when you finsh this order write 1"))
         if que=="1":
             food2.dequeue()
             print( "  finshed succesfully ")
             break
    elif menu=="3":
        opn=input("Are you sure you want delet the last order 1 :\n")
        if opn=="1":
            print(f" we succesfully deleted this order {food1.peak1()}")
            food1.pop()
