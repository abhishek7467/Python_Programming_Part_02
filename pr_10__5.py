class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("\n ****** \n")
        print(f"The name of the Train is :  {self.name}")
        print(f"The Seats are availabhle in the trin:  {self.seats}")
        print("\n ******* \n")
    def fareInfo(self):
        print(f"The prince of the ticket is :  Rs {self.fare}") 
    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked !  your seat number is {self.seats}")
            self.seats = self.seats-1
        
        else:
            print("Sorry this train is full")    
    def cancelTicket(self):
        pass
    

intercity=Train("Intercity Express", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.fareInfo()               
