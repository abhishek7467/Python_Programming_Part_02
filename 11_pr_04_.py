
# formula for this pr.. ->  (a+bi)(c+di) = (ac-bd) + (ad-bc)
class ComplexNumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return ComplexNumber(self.real + c.real, self.imaginary+c.imaginary)

    def __mul__(self,c):
        mulReal= self.real*c.real-self.imaginary*c.imaginary
        mulImaginary= self.real*c.imaginary+self.imaginary*c.real
        return ComplexNumber(mulReal, mulImaginary)


    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {- self.imaginary}i"
        else:    
            return f"{self.real} + {self.imaginary}i"        

c1 = ComplexNumber(1,4)
c2 = ComplexNumber(8,5)        
print(c1 + c2)
print(c1 * c2)