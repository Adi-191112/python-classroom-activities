class vehicle:
     def __init__(self,capacity):
        self.capacity = capacity

     def fare(self):
         return self.capacity*100
          
     


class bus (vehicle):
    def fare(self):
        base = super().fare()
        maintanance = base*0.1
        return base + maintanance
    
object = bus(50)
print("the total bus fare is ", object.fare())
