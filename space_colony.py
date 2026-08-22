class System:
    def __init__(self,name,food,water,energy,money):
        self.name=name
        self.food=food
        self.water=water
        self.money=money
        self.energy=energy
    def __str__(self):
         return f" this colony is {self.name} **********food is {self.food}*************water is {self.water}***** energy is {self.energy} and the balance is {self.money}"
    def increase_food (self,amount):
          self.food+=amount
    def increase_water(self,amount):
         self.water+=amount
    def increase_energy(self,amount):
         self.energy+=amount
    def increase_money(self,amount):
         self.money+=amount
    def decrease_food(self,amount):
         if self.food>amount:
              self.food-=amount
              return True
         else:
              return False
   
    def decrease_water(self,amount):
          if self.water>amount:
             self.water-=amount
             return True
          else:
             return False
          
    def decrease_energy(self,amount):
             if self.energy>amount:
                  self.energy-=amount
                  return True
             else:
                  return False

    def decrease_money(self,amount):
         if self.money>amount:
              self.money-=amount
              return True
         else:
              return False

class Employs:
     def __init__(self,name,health):
          self.name=name
          self.health=health

     def increase_health(self,amount):
          self.health+=amount
     def decrease_health(self,amount):
          if self.health>=0 and self.health>=amount:
               self.health-=amount
               return True
          else  :

               return False
     def change_state(self,amount):
               check_h=self.decrease_health(amount)
               if check_h:
         
        
                 return True
               else:
                return False
     
class Farmer(Employs):
     def __init__(self,name,health):
          super().__init__(name,health)
     def work(self):
          check1=self.change_state(50)
          if check1:
               system1.increase_food(100)
               if system1.decrease_money(100):
                    return 
               else:
                    print("we don't have enough resorce")
               
                    
               if system1.decrease_energy(100):
                    return 
               else:
                    print("we don't have enough resorce")
               system1.increase_water(100)
               
               return True
          else :
             
               return False
class Scientist(Employs):
      def __init__(self,name,health):
               super().__init__(name,health)
      def work(self):
               check1=self.change_state(50)
               if check1:
                    if system1.decrease_food(100):
                     return
                    else:
                         print("we don't have enough resorce")
                    system1.increase_money(100)
                    system1.increase_energy(100)
                    system1.increase_water(100)
                    
                    return True
               else :
                   
                    return False

class Doctors(Employs):
     def __init__(self,name,health):
                    super().__init__(name,health)
     def work(self):
                    check1=self.change_state(50)
                    if check1:
                         self.increase_health(60)
                         if system1.decrease_food(100):
                             
                              if system1.decrease_money(100):
                                   
                                   if system1.decrease_energy(100):
                                       
                                        if system1.decrease_water(100):
                                             return
                         else:
                              print("we don't have enough resource")
                        


system1=System("mars colony",100,100,100,100)
farmer1=Farmer("MAhmoud",300)
scientist1=Scientist("Ali",300)
doctor1=Doctors("aml",500)


while True:
     menu=input(" show items 1 , use fermer 2 , use scientist 3 , log out 4")
     if menu =="1":
          print(system1)
     elif menu=="2":
          check2=farmer1.work()
          if check2:
            print("*****************")
            print("succesfull ")
            print(system1)
          else:
               print("I want rest")
               while True:
                 
                 answer=input("Do you want use doctor yes 1 No 2")
                 if answer=="1":
                  doctor1.work()
                  break
                 elif answer=="2":
                      print("so I cant't do this task sorry ")
                      break
                      
     elif menu=="3":
          check3=scientist1.work()
          if check3:
               print("***********")
               print("succesfull")
               print(system1)
          else:
               print(" I want rest")
                 
               while True:
                                
                                answer=input("Do you want use doctor yes 1 No 2")
                                if answer=="1":
                                 doctor1.work()
                                 break
                                elif answer=="2":
                                     print("so I cant't do this task sorry ")
                                     break
     else:
          break