numGrades = int (input ('How many grades ? '))
Grades = []
add = 0
lowGrade = 100
highGrade = 0

swp=0

for i in range (0,numGrades,1):
    grade = float (input ('Enter your grade: '))
    Grades.append(grade)
print ('Your Grades Are: ', Grades)

for i in range (0,numGrades,1):
    add= add + Grades[i]
   
avg = add/numGrades

print ('Your Average Grade is' , avg)


for i in range (0,numGrades,1):
    if (Grades[i] <= lowGrade):
        lowGrade = Grades [i]

print ('lower grade is:' ,lowGrade)

for i in range (0,numGrades,1):
    if (Grades[i] >= highGrade):
        highGrade = Grades [i]

print ('Higher grade is: ', highGrade)

for i in range (0,numGrades-1, 1):
    for i in range (0,numGrades-1, 1):
        if  (Grades[i]<Grades[i+1]):
            swp = Grades[i]
            Grades[i]=Grades[i+1]
            Grades[i+1]=swp
print ('The sorted Table is: ',Grades)