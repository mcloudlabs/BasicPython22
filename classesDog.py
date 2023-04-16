class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        pass
    def get_name (self):
        return self.name
    
    def get_breed (self):
        return self.breed

    def add_one(self,x):
        return x+1

    def bark(self):
        print ('Bark')

d=Dog('tim','rotty')
d2 = Dog('bill','pitbull')

print(d.bark())
print (d.add_one(5))
print (d.get_breed())
print (d2.get_breed())