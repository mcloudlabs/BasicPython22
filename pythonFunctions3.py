def tally (nums):
    x=[]
    for i in range(0,nums,1):
        myNum=float(input('Enter your number  '))
        x.append(myNum)
    return x #important otherwise the function will not return the result



a=int(input('Please input how many number  '))
y= tally (a) 

print (y)