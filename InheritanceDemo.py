class Car:# Parent class or Super class
    def __init__(self, color, wheel_count): # initiatlize attributes
        self.color = color
        self.wheel_count = wheel_count
    def validate(self): # method definition
        if self.wheel_count == 4:
            return 'This is a car'
        else:
            return 'This is NOT a car'
        
class Truck: # Another parent class
    def func(self):
        print("This is from Car2 class")

class Tesla(Car): #Single inheritance - Child class inheriting parent class
    def __init__(self,color, wheel_count,engine):
        super().__init__(color, wheel_count)
        self.engine =  engine

class Roadster(Tesla):#Multi-level Inheritance - Child class inheriting from another child class
    def __init__(self,color, wheel_count,engine,drive):
        super().__init__(color,wheel_count,engine)
        self.drive = drive

class Hybrid(Car,Truck): # Multiple Inheritance - Child class inheriting from two parent class
    pass
        
car1 = Tesla("Blue", 6, "Electric") # Object created from single inherited child class
print(car1.validate()) # access method from parent class through child class

car2 = Roadster("Red",4,"Electric","4WD") # object created from multilevel inherited child class
print(car2.drive) # access attribute from child class
print(car2.engine) # access attribute from 1 level up parent class
print(car2.validate()) # access method from 2 level up parent class

car3 = Hybrid("Black", 4) # Object created from multiple inherited child class
print(car3.validate()) # access method from one of the parent class
car3.func() # access method from another parent class
