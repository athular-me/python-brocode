class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    #using methods 
    def drive(self):
        print(f"you are driving {self.model}")
    def stop(self):
        print(f"you are braking {self.model}")
car1=Car("Tesla",2025,"Red",False)
car2=Car("BMW",2015,"White",True)


print(car1.color)
print(car1.model)
print(car2.year)
print(car2.for_sale)
car1.drive()
car2.stop()