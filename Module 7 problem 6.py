# Jessica Kusmierz
# 11/6/2025
# Problem 6

class car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        def get_model(self:):
            return self.model
        
    def get_year(self:):
        return self.year
    
    def get_Color(self):
        return self.color
    
    def fullspecs(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"
    
    Car1 = car("sports", 2012 , "Blue")
    Car1.color = "Red"
    print(Car1.fullspecs())
    Car2 = car("sedan", 2020 , "Black")
    Car2.color = "Blue"
    print(Car2.fullspecs())
    

print(car1.get_model())
print(car1.get_year())
print(car1.get_Color())
print(car1.fullspecs())

print(car2.get_model())
print(car2.get_year())
print(car2.get_Color())
print(car2.fullspecs())
