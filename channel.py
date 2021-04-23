from bitarray import bitarray
import random


class Channel:
    def __init__(self, array, probability):
        self.length = len(array)
        self.distorted_array = bitarray(self.length)
        self.probability = probability
        self.distort(array)

    def distort(self, array):
        for i in range(self.length):
            if(random.randint(0, 100)/100 < self.probability):
                if(array[i] == 0):
                    self.distorted_array[i] = 1
                else:
                    self.distorted_array[i] = 0
            else:
                self.distorted_array[i] = array[i]
