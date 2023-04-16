class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1 # Keep track on how many instance of this classes we have created

p1 = Person ('tim')
print (Person.number_of_people)
p2 = Person ('jill')
print (Person.number_of_people)

