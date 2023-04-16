myNumber = float (input ('Please enter your number:  '))
rem = myNumber % 2 

if (myNumber > 0 and rem == 0):
    print ('Congratulations! Your Number is Even Positive')
if (myNumber < 0 and rem == 0):
    print ('Congratulations! Your Number is Even Negative')
if (myNumber < 0 and rem == 1):
    print ('Congratulations! Your Number is Odd Negative')
if (myNumber > 0 and rem == 1):
    print ('Congratulations! Your Number is Odd Positive')
if (myNumber == 0):
    print ('Oops! Your numer is 0')