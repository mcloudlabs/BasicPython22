numGrades = int (input ('How many grades ? '))
Grades = []
add = 0
lowGrade = 100
highGrade = 0
for i in range (0,numGrades,1):
    grade = float (input ('Enter your grade: '))
    Grades.append(grade)
print (Grades)

for i in range (0,numGrades,1):
    add= add + Grades[i]
    print (add)

avg = add/numGrades

print (avg)


for i in range (0,numGrades,1):
    if (Grades[i] <= lowGrade):
        lowGrade = Grades [i]

print (lowGrade)

for i in range (0,numGrades,1):
    if (Grades[i] >= highGrade):
        highGrade = Grades [i]

print (highGrade)