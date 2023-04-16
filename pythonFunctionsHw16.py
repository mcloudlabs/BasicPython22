def inputGrades(numGrades):
    grades=[]
    for i in range (0,numGrades,1):
        grade=float(input('enter Grade:  '))
        grades.append(grade)
    return grades

def printGrades(numGrades,grades):
    for i in range (0,numGrades,1):
        print (grades[i])


def avGrades(numGrades,grades):
    tot = 0
    for i in range (0,numGrades,1):
        tot = tot + grades[i]
    avg = tot / numGrades
    return avg

def highLow(numGrades, grades):
    lowGrade = 100
    highGrade = 0
    
    for i in range (0,numGrades,1):
        if (grades[i] <= lowGrade):
            lowGrade = grades [i]

    for i in range (0,numGrades,1):
        if (grades[i] >= highGrade):
            highGrade = grades [i]

    return lowGrade, highGrade

numGrades = int (input ('How many grades ? '))
finalGrades = []
print ('')


finalGrades = inputGrades(numGrades)
print (finalGrades)
print('')

printGrades (numGrades,finalGrades)
print('')

average = avGrades (numGrades, finalGrades)
print ('The Average is:  ', round (average,2))

print('')
low,high = highLow (numGrades, finalGrades)
print ('highest grade is: ',high)
print('lowest grade is: ',low)