class animal:
    def __init__(self,name):
        self.name=name
    pass
class dog(animal):
    pass
class cat(dog):
    pass
class fish(dog,cat):
    pass
