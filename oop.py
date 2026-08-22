class Account:
    def __init__(self,name,balance ,password):
        self.name=name
        self.balance=balance
        self.__password=password
        
    def __str__(self):
        return f"Hi mr {self.name} your balance is {self.balance}"
    def deposit(self,amount1):
        if amount1>0:
            self.balance+=amount1
            return True
        else:
            return False
    def withdraw(self,amount2):
        if amount2>self.balance:
            print("you don't have enough")
            return 
        elif amount2<=0:
            return False
        else :
            self.balance-=amount2
            return True
    def check(self, password):
         return password==self.__password
    

class Saving_Account(Account):
    def __init__(self,type):
        self.type=type
    def grow(self):
        if self.balance>1000:
            grow=self.balance*0.1
            self.balance+=grow
    def ch(self) :
        return self.type=="1"
              
        
class Bank:
    
    def __init__(self,name):
        self.name=name
        self.accounts=[]
    def add(self, account):
        self.accounts.append(account)
        return
    def login(self, entered_pass):
       
        
            
            for acc in self.accounts:
                if acc.check(entered_pass):
                 return acc
            return None


bank1=Bank("Misr")

while True:
     main_menu=input("add acount 1 , login 2 , leave 3\n")
     if main_menu=="1":
       name=input("what's your name:\n")
       balance=int(input(" How much do you have:\n"))
       password=input("enter the pass").lower()
       
       account1=Account(name,balance,password)
       bank1.add(account1)
       type_a=input("what type of your account 1 saving 2 busniss :\n")
       save1=Saving_Account(type_a)
       if save1.ch():
           save1.grow()
      
     elif main_menu=="2":
          if len(bank1.accounts)==0:
                     print("no data")
          else:
           entered_pass=input("entre the pass")
           current_account=bank1.login(entered_pass)
         
           if current_account:
             print(current_account)
             print("********************************")
             while True :
                 choose=input("show balance 1 , deposite 2 , withdraw 3 , leave 4:\n")
                 if choose=="1":
                     print(f"your balance now is {current_account.balance}")
                     print(current_account.__password)
                 elif choose=="2":
                     while True :
                         try:
                          amount=int(input("enrer numbers:\n"))
                          succes=current_account.deposit(amount)
                          if succes:
                              print("deposite succes")
                              break
                          else:
                              print("invild data")
                          break
                         except:
                             print ("wrong data")
                 elif choose=="3":
                     while True:
                         try:
                          amont9=int(input("enter numbers:\n"))
                          sucess2= current_account.withdraw(amont9)
                          if sucess2:
                              print("withdraw succes")
                              break
                          else:
                              print("invaild data")
                          break
                         except:
                             print("wrong data")
                 elif choose=="4":
                     break
                 else:
                     print("wrong input")
           else : 
             print("wrong pass")
     elif main_menu=="3":
         print("hello")