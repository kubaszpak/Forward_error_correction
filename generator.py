from bitarray import bitarray
import random


class Generator:
    def __init__(self):
        pass

    def populate_array(self, _len):
        rand_bitarray = bitarray(_len)
        for i in range(_len):
            rand_bitarray[i] = random.randint(0, 1)
        return rand_bitarray
