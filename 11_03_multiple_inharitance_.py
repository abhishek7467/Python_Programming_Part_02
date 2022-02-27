class Employee:
    company="Visa"
    eCode=120

class Freelancer:
    company="Fiver"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="Rohit"
p=Programmer()

p.upgradeLevel()
print(p.name)
print(p.level)
print(p.company)
l=Freelancer()
print(l.company)    