import pickle
with open('myPickleStudentData.pkl','rb') as Dataf:
    numStudents=pickle.load(Dataf)
    names=pickle.load(Dataf)
    grades=pickle.load(Dataf)

print(numStudents)
print(names)
print(grades)

while (1==1):
    name=input('which student you want to check?   ')
    for i in range(0,numStudents,1):
        if names[i] == name:
            print (name, 'Grade is ', grades[i],'  is  ')
            print ('To avoid space concatenate strings',str(name), 'Grade is ', str(grades[i]),'  is  ')