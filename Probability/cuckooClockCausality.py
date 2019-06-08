import numpy as np
from IPython.display import clear_output
import time
from typing import Callable

class Button: 
    def __init__(self,clickTime:Callable[[int],bool]):
        # A bool
        self.clickTime = clickTime
        self.time = 0
    def sample(self,endTime):
        ls = []
        for i in range(endTime):
            ls.append(self.clickTime(i))
        return np.array(ls)

class CuckooClock: 
    def __init__(self,isOut:Callable[[int,Button],bool], button:Button):
        # A bool
        self.isOut = isOut
        self.button = button
        self.time = 0

    def tick(self):
        self.time += 1
    
    def run(self,speed=.5,timeLimit=100):
        for i in range(timeLimit):
            clear_output()
            self.tick()
            if self.isOut(self.time,self.button):
                print("{0} Coo Coo!".format(self.time))
            else: 
                print("{0}".format(self.time))
            time.sleep(speed)

    def sample(self,timeLimit=100) -> np.array:
        clockData = []
        buttonData = [] 
        
        for i in range(timeLimit):
            self.tick()
            clockData.append(self.isOut(self.time,self.button))
            buttonData.append(self.button.clickTime(self.time))
        
        return np.stack((clockData,buttonData),0)




