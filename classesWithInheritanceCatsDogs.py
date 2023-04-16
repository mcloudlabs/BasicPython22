class Pet:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def show (self):
        print (f"I am {self.name} and I am {self.age} years old")

class Dog(Pet): #add the parent class (Pet) as parameter fot the child class.
    def speak(self): # if the a method with same name is on the parent  the child will be retained
        print('Bark')

class Cat(Pet):
    def __init__(self, name, age,color): # if we need to have more attribure we reuse __init and add super()
        super().__init__(name, age)
        self.color = color

    def speak (self):
        print('Meow')
    def show (self):
        print (f"I am {self.name} and I am {self.age} years old and I am {self.color}")

p= Pet ('tim', 10)
p.show()
# p.speak() is not available in the parent thus will not reflect here 

c=Cat ('Bill', 8, 'red')
c.show()
c.speak()

d=Dog('Ace',3)
d.show()
d.speak()