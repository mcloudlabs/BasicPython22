class Student:
    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName

    def InputGrade (self,NumGrades):
        self.grades = []
        for i in range (0,NumGrades,1):
            self.grade = float (input ('Please enter your grade for student {self.name} :'))
            self.grades.append(self.grade)
        return self.grades

    def listGrades (self,numGrades, grades):
        for i in range (0,numGrades,1):
            print (self.grades[i])

    def average (self,numGrades, grades):
        tot=0
        for i in range (0,numGrades,1):
            tot += grades[i]
        self.avg= tot/numGrades
        return self.avg

s1=Student('Mounir','Mel')
s2=Student('Sarah','Mel')
grades=[]

numGrades = int (input ('how many Grades'))
s1Grade= s1.InputGrade(numGrades)
print (s1Grade)
s2Grade= s2.InputGrade(numGrades)
print (s2Grade)

s1.listGrades(numGrades,s1Grade)

avg2 = s2.average(numGrades, s2Grade)
print (avg2)


