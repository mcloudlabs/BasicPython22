#Input two numbers and sum them together

#Define the function with def / variable name dont have to match the name when u call

def tally (num,myArray):
    tot=0
    for i in range (0,num,1):
        tot = tot + myArray[i]
    return tot #important otherwise the function will not return the result

nums =5
x=[2,4,6,8,10]

mySum=tally(nums,x)

print ('Array total is:  ', mySum)