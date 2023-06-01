# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
class Base:
 
    # Constructor
    def __init__(self, name):
        self.name = name
        # d is private instance variable cannot be accessed outside the class.
        self.__d = 42
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
 
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
 
 
class GrandChild(Child):
 
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
        # inheriting the properties of parent classes both child and base class.
        super().__init__("Rahul", 40)
 
    # To get address
    def getAddress(self):
        return self.address
 
 
# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName())
print(g.getName(), g.getAge(), g.getAddress())