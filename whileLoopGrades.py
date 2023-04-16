numGrades = int(input ('How many grades you have?  '))
grades = []
j=0

while (j<numGrades):
    grade = float(input('enter your grade'))
    grades.append(grade)
    j=j+1

print(grades)
j=0
while (j<numGrades):
    print(grades[j])
    j=j+1
print ('Thats all Folks')