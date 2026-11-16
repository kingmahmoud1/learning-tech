class Rast:
    def __init__(self,balance,amount,name):
        self.name=name
        self._balance=balance
        self.amount=amount
    def use(self,us):
        tem=self.amount-us
        if tem>=0:
            print (" you succesfully added your order") , 
            return tem , True
        else:
            print ("we don't have enough amount")  
            return False
    
    def add_balance(self,add):

        if self.use(add):
            self._balance= self._balance+add
mac=Rast(100,200,"mac")
mac.add_balance(300)