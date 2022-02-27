class Preson:
    countery="India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Preson):
    company="Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so i am luckly breathing..")

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")
    def takeBreath(self):
        print("I am Programmer so i am luckly breathing..")    

p=Preson()
p.takeBreath()
#print(p.company)
e=Employee()
print(e.company)
e.takeBreath()
pr=Programmer()
print(pr.company)
pr.takeBreath()
print(p.countery)


