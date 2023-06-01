class Addition:
    first = 0
    second = 0
    answer = 0
 
    # parameterized constructor
    def __init__(self, f=None, s=None):
        # If no arguments are passed for both the default value is used.
        if f is None and s is None :
            self.second = 10
            self.first = 10
        else:
            self.first = f
            self.second = s
 
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
        self.answer = self.first + self.second
 
 
# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)
 
# creating second object of same class
obj2 = Addition(10, 20)

# creating third object of same class
obj3 = Addition()

# perform Addition on obj1
obj1.calculate()
 
# perform Addition on obj2
obj2.calculate()

# perform Addition on obj3
obj3.calculate()
 
# display result of obj1
obj1.display()
 
# display result of obj2
obj2.display()

# display result of obj3
obj3.display()
 