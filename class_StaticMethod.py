class Math:
    @staticmethod
    def add5(x): #act as  function that is defined in this class.
        return x+5

    @staticmethod
    def add10(x): #act as  function that is defined in this class.
        return x+1
    
    @staticmethod
    def pr():
        print ('Run')

print (Math.add5(10))
print (Math.add10(10))
Math.pr()