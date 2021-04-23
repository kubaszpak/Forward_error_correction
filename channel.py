from bitarray import bitarray
import random
from numpy import *


class Channel:
    def __init__(self, array, probability):
        self.distorted_array = array.copy()
        self.length = len(array)
        self.probability = probability
        self.distort()


    def distort(self):
        for i in range(self.length):
            if(random.randint(0,100) <= self.probability*100):
                if(self.distorted_array[i] == 0 ):
                    self.distorted_array[i] = 1
                else: 
                    self.distorted_array[i] = 0