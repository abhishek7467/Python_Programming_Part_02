import pandas as pd
pd.DataFrame()

class RailWay:
    formType="RailwayForm"
    def printData(self):
        print(f"namw is {self.name}")
        print(f"Train is {self.train}")


Application = RailWay() 
Application.name = "Abhishek"
Application.train ="NEW Tairm"
Application.printData()   




'''a=12
b=34

print(a+b)
'''

