import pickle

print ('Dont numae you prorgame pickle.py it will confuse python')

fruits=['apple','Oranges','banana']
x=7
y=3.14
nuts=['pecans','almonds']
grades=[99,100,77,56,85]

dataSet=[fruits,x,y,nuts,grades]

with open ('myData.pkl','wb') as f:
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
    pickle.dump(dataSet,f)


with open ('myData.pkl','rb') as f2:
    a=pickle.load(f2)
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)
    fullDataSet=pickle.load(f2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(fullDataSet)

print ('Printing Full Data set per item')

for dt in fullDataSet:
    print (dt)