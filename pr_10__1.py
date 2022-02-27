class Programmer:
    company="Moicrosoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and product is {self.product}") 
        
abhishek=Programmer("allow", "skype")        
alka=Programmer("Alka", "Drive")
abhishek.getInfo()
alka.getInfo()