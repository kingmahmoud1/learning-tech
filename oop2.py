class Station:
    def __init__(self,name,health,budget):
        self.name=name
        self.health=health
        self.budget=budget
    def salary(self,amount):
        if self.budget>=amount:
            self.budget-=amount
            return True
        else:
            return False
    def use_health(self,using):
        if self.health>=using:
            self.health-=using
            return True
        else:
            return False
    def Maintenance(self,main):
        self.health+=main
class poilt:
    def __init__(self,name):
        self.name=name

    def make_trip(self):
               amount1=current_plane.using_money
               using_h=current_plane.using_health
               check1= station1.salary(amount1)
               
               if check1:
                   check2=station1.use_health(using_h)
                   if check2:
                       print("succesfull trip")

               else:
                   print("please make maintance")

class maintance:
    def __init__(self,name):
        self.name=name
    def make_main(self):
                main1=10
                station1.Maintenance(main1)
                station1.salary(100)


class planes:
     def __init__(self,name , using_money,using_health):
          self.name=name
          self. using_money= using_money
          self.using_health=using_health
     def check_p(self,name):
          return self.name==name
        

plane1=planes("cs50",100,5)
plane2=planes("cs23",200,10)
plane3=planes("cs34",300,15)
list_p=[plane1,plane2,plane3]

                

station1=Station("cairo station", 100, 5000000)
poilt1=poilt("mahmoud")
main12=maintance("Ahmed")
#menu
while True :
    menu=input("new trip 1 , maintance 2 , show balance and health 3 , log out 4:\n")
    if menu=="1":
        name=input("which plane do you want:\n").lower()
        for acc in list_p:
         if acc.check_p(name):
          current_plane=acc 
        poilt1.make_trip()
      
    if menu=="2":
       main12.make_main()
    if menu=="3":
        print(f" there are {station1.budget} in the station")
        print(f"station health is{station1.health}")
    if menu=="4":
        break