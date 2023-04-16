import pickle

names=[]
grades=[]

numStudents=int(input('How many student you have? '))

for j in range (0,numStudents,1):
    name = input('Please enter the student name:  ')
    names.append(name)
    prompt = 'Please enter '+ name +"'s Avg Grade:  "
    grade = float (input(prompt))
    grades.append(grade)

print(names)
print(grades)

with open('myPickleStudentData.pkl','wb') as dataFile:
    pickle.dump(numStudents,dataFile) 
    pickle.dump(names,dataFile)
    pickle.dump(grades,dataFile)

with open('myPickleStudentData.pkl','rb') as readFile:
    a=pickle.load(readFile)
    b=pickle.load(readFile)
    c=pickle.load(readFile)
print(a,b,c)