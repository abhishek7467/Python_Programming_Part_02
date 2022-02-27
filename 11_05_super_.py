class Preson:
    def __init__(self):
        print("Initializing person....\n")

    countery="india"    

    def takeBreath(self):
        print("I am breathing...")

class Employee(Preson):
    company="Honda"
    def __init__(self):
        super( ).__init__()
        print("Initializing Employee....\n")


    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so i am luckly breathing..")

class Programmer(Employee):
    company="Fiverr"

    def __init__(self):
        #super( ).__init__()
        print("Initializing Programmer....\n")

    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
        super().takeBreath()
        print("I am Programmer so i am luckly breathing..")    

#p=Preson()
#p.takeBreath()

#e=Employee()
#e.takeBreath()

pr=Programmer()
#  pr.takeBreath()


