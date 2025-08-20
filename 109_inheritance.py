class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    pass
    def sleep(self):
        print(f"{self.name} is sleeping...")
        pass
    def eat(self):
        print(f"{self.name} is eating...")
        pass
class dog(animal):

    pass
class cat(animal):
    pass
dog1=dog("Jack")
cat1=cat("Mittu")
cat1.sleep()
dog1.eat()

