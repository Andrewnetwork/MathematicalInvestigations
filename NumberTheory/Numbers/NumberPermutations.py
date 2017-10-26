import numpy as np


# TODO FIX
def numPermutations(digits, base):

    lst = []
    iteration = 0
    cond = True

    while cond:
        if iteration == 0:
            lst.append( (digits ** base, base) )
        else:
            lst.append( ( ( digits**base)/(iteration*base) , base**(iteration) ) )
            if((digits**base)/(iteration*base) == 1):
                return lst

        iteration += 1


for i in range(1,10):
    print( numPermutations(i,2) )
