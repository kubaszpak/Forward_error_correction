from bitarray import bitarray
import random


class Channel:
    def __init__(self, probability):
        self.probability = probability

    def distort(self, array):
        _len = len(array)
        distorted_array = array.copy()
        for i in range(_len):
            if(random.randint(0, 100)/100 < self.probability):
                distorted_array[i] = distorted_array[i] ^ 1
        return distorted_array
