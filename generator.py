from bitarray import bitarray
import random


class Generator:
    def __init__(self, length):
        self.bit_array = bitarray(length)
        self.length = length
        self.populate_array()

    def populate_array(self):
        for i in range(self.length):
            self.bit_array[i] = random.randint(0, 1)
