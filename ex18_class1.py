#Create a class 'dog' with class variable, instance variable and methods.

class Dog:
    #pass is used to create an empty class
    #class variable
    animal = 'dog'

    # init method/ constructor
    def __init__(self, breed, color, age):

        #Instance variable
        self.breed = breed
        self.color = color
        self.age = age

    #define how a class object should be represented as a string
    def __str__(self):

        return f"The breed of {self.animal} is {self.breed} and color is {self.color}."

    # define a method.
    def displayAge(self):
        print('The age is', self.age)

# Objects of Dog class
Rodger = Dog("Pug", "brown", 4)
Buzo = Dog("Bulldog", "black", 7)
 
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
Rodger.displayAge()

print('Buzo details:')
print(Buzo)
Buzo.displayAge()
    
