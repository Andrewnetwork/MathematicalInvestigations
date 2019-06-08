# cuckooClockCausality.py
# Andrew Ribeiro 
# June 2019 

import numpy as np
from IPython.display import clear_output
import time
from typing import Callable

class CausalityModel:
    def causalViolation(self,sample)->bool:
        """
        Checks if given a sample, a 2xN boolean matrix, contains a causal violation. 
        Namely, it check if the casual signal occurs before event signal. 
        """
        return True

        

class Button:
    def __init__(self,clickTime:Callable[[int],bool]):
        """
        Args: 
        - clickTime(time) -> button is pressed at the given time
        """
        self.clickTime = clickTime
    def sample(self,endTime)->np.array:
        """
        Produces a boolean array by evaluating clickTime on [0,endTime).
        """
        ls = []
        for i in range(endTime):
            ls.append(self.clickTime(i))
        return np.array(ls)

class CuckooClock: 
    """
    A class initialized 
    """
    def __init__(self,isOut:Callable[[int,Button],bool], button:Button):
        """
        Args: 
        - isOut(time,button) -> cuckoo bird is out of the clock. 
        """
        # A bool
        self.isOut = isOut
        self.button = button
        self.initClock()

    def tick(self):
        self.time += 1
    
    def run(self,speed=.5,timeLimit=100):
        self.initClock()
        for _ in range(timeLimit):
            clear_output(True)
            self.tick()
            if self.isOut(self.time,self.button):
                if self.button.clickTime(self.time):
                    print("{0} Coo Coo! (button pressed)".format(self.time))
                else:
                    print("{0} Coo Coo!".format(self.time))
            else: 
                print("{0}".format(self.time))
            time.sleep(speed)

    def sample(self,timeLimit=100) -> np.array:
        clockData = []
        buttonData = [] 
        self.initClock()

        for _ in range(timeLimit):
            self.tick()
            clockData.append(self.isOut(self.time,self.button))
            buttonData.append(self.button.clickTime(self.time))
        
        return np.stack((clockData,buttonData),0)

    def initClock(self):
        self.time = 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()

