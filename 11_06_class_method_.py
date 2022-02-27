class Employee:
    compney="Camel"
    salary=100
    location="Delhi"

    #def changeSalary(self,sal):
     #   self.__class__.salary=sal
    @classmethod 

    def changeSalary(cls,sal):
    
        cls.salary=sal    


e=Employee()
print(e.salary)    
e.changeSalary(189)
print(e.salary)
print(Employee.salary)