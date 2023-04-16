class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def gradesInput (self,ng):
        self.ng=ng
        self.grades=[]
        for i in range (0,self.ng,1):
            grd = float (input ('Enter Grade'))
            self.grades.append(grd)
        return self.grades
    
    def printGrades(self):
        print (self.first, self.last, ' grade are')
        for i in range (0,self.ng,1):
            print (self.grades[i])
        print ('')
    def avGrades (self):
        tot = 0
        for i in range (0,self.ng,1):
            tot = tot + self.grades[i]
        avg = tot/self.ng
        return avg
    def highLowGrades (self):
        highGrade =0
        lowGrade=100
        for i in range (0,self.ng,1):
            if (self.grades[i]>highGrade):
                highGrade=self.grades[i]
            if (self.grades[i]<lowGrade):
                lowGrade=self.grades[i]
        return lowGrade,highGrade


student1 = Students('Mounir','Mel')
student2 = Students('Sarah','Mel')
print (student1.first,student1.last)
student1.gradesInput(2)

print (student2.first,student2.last)
s2Grades= student2.gradesInput(2) # Student 2 working with the return function of the method that returns self.grades

print (student1.grades) #Student 1 refer to the variable self.grades straight
print (s2Grades)

student1.printGrades()

print (student1.avGrades())

lowG,highG = student1.highLowGrades()
print('low grade is', lowG)
print('high grade is',highG)