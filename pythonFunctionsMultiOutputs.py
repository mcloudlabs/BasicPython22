def tally (x,y):
    tot=x+y
    dif=x-y
    prod=x*y
    div=x/y

    return tot,dif,prod,div

a=float(input ('enter first num:   '))
b=float(input ('enter second num:  '))

w,x,y,z=tally(a,b)

print (w)
print(x)
print(y)
print(z)
