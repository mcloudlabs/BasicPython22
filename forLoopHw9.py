numGrades = int (input ('Please enter the number of grades: '))
grades = []
add = 0
for i in range (0,numGrades,1):
    grade = float (input('Please enter the grade: '))
    grades.append(grade)

print ('Your Grdes Are: ' ,grades)

for i in range (0,numGrades,1):
    add = add + grades[i]

print ('sum of notes is:  ', add)

avg = add / numGrades

print ('Average is:  ', add,' / ',numGrades, ' = ', avg)