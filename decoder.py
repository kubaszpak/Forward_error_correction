from bitarray import bitarray
import random


class Decoder:
    def __init__(self, array):
        self.length = (len(array))//3
        self.decoded_array = bitarray(self.length)
        self.decode(array)

    def decode(self, array_to_decode):
        for i in range(0, len(array_to_decode), 3):
            one_counter = array_to_decode[i] + \
                array_to_decode[i+1] + array_to_decode[i+2]

            if(one_counter >= 2):
                self.decoded_array[i//3] = 1
            else:
                self.decoded_array[i//3] = 0
