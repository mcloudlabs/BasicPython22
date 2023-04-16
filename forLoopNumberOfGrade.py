numGrades= int(input('Please enter the number of grade: '))
grades = []
for i in range (0,numGrades,1):
    grade = float (input ('Please enter the grade'))
    grades.append(grade)
print (grades)

for grade in grades:
    print (grade)

for i in range (0,numGrades,1):
    print (i)
    print (grades[i])

print('Thats All Folks')