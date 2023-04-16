#Input two numbers and sum them together

#Define the function with def / variable name dont have to match the name when u call

def tally (x,y):
    z=x+y
    a=10 # this a and b variable have a scope of the function unless returned they will stay inside the funtion
    b=12 # this variable will not conflict with a and b in main program
    print ('a inside function is ',a,'and b inside function is ', b)
    return z #important otherwise the function will not return the result



a=float(input('Please input your first number:  '))
b=float(input('Please input your Second number:  '))

c= tally (a,b) #z is calling tally
print ('sum is ', c)