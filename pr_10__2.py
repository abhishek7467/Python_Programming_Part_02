class Calculator:
    def __init__(self,num):
        self.number=num
    def squar(self):
        print(f"The value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")
    def Cube(self):
          print(f"The value of {self.number} Cube is {self.number **3}")    
a=Calculator(2)
a.squar()
a.squareRoot()
a.Cube()          