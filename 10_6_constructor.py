class Employee:
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The name of the employee is {self.salary}")
        print(f"The name of the employee is {self.subunit}")
    def getsalary(self,signature):
            print(f"salary for this employee is {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet():
        print("Good morning everyone")
    @staticmethod
    def time():
        print("The time is 9 Am in the morning")
#harry=Employee()        
harry=Employee("abhishek", 10000, "Youtube")
harry.getDetails()
harry.greet()

