# Port from my C++ Version
# https://github.com/Andrewnetwork/breaking-the-code/blob/master/AndrewWork/Server/HeftyCounter.cpp

import numpy as np

class HeftyCounter:
    def __init__(self,length,base):
        self.base = base
        self.counterSize = length
        self.counter = np.zeros(length)

    def increment(self, quantity ):

        if quantity != 0:
            remainder         = quantity
            additionRemainder = 0
            counterIndex      = 0
            additionTemp      = 0
            digitCount        = 1
            cond              = True

            #Convert quantity to the counters base and add it to the counter at the same time.
            while cond:
                counterIndex = self.counterSize - digitCount
                additionTemp = (self.counter[counterIndex] + (remainder % self.base) + additionRemainder)
                self.counter[counterIndex] = additionTemp % self.base
                additionRemainder = int(additionTemp) / int(self.base)
                remainder = remainder / self.base

                if (additionRemainder > 0 or remainder > 0) and digitCount >= self.counterSize :
                    #Overflow.
                    self.counter = np.insert(self.counter,0,0)
                    self.counterSize += 1

                digitCount+=1

                cond = remainder > 0 or additionRemainder > 0


