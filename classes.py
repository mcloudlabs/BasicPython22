class Rectangle: # in Class we do ot pass parameters
    #Every Class should have functions to set things up
    def __init__(self,c,l,w):  #Function inside a class is called a method, Eveytime I need an init method
        self.color=c
        self.lenght=l
        self.width=w
    def area(self):
        self.area=self.lenght * self.width
        return self.area

    def perim(self):
        self.perim = 2*(self.lenght+self.width)
        return self.perim

    def diagonal(self):
        self.diag = (self.width**2+self.lenght**2)**(1/2)
        return self.diag

    def volume (self,h): #Passing parameters that are not part of the initial set up
        self.height=h
        self.vol = self.lenght*self.width*self.height
        return self.vol


#Create the Objects to be able to call the methods of that objects 
myRect1=Rectangle('red',2,4) 
myRect2=Rectangle('blue',5,3)


print (myRect1.color)
print (myRect2.color)
print ('my rec1 area', myRect1.area())
##print ('my rec1 area', myRect1.area())

area2=myRect2.area()
print ('my rec2 area', area2)

print ('my rec1 perim', myRect1.perim())
print ('my rec2 perim', myRect2.perim())

print ('my rec1 Diagonal', myRect1.diagonal())
print ('my rec1 volume', myRect1.volume(5))