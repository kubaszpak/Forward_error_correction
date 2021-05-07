from bitarray import bitarray
import bchlib


class Coder:
    def __init__(self):
        self.length = len(array) * 3
        self.triple_array = bitarray(self.length)
    
    def triple_code(self, array):
        for i in range(0, self.length, 3):
            self.triple_array[i] = array[i // 3]
            self.triple_array[i+1] = array[i // 3]
            self.triple_array[i+2] = array[i // 3]

    def bch_code(self, array, polynomial_degree):
        bch = bchlib.BCH(polynomial_degreeL, len(array))
        bch_array = bch.encode(array)
        return bch_array

    def access_bit(data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] & (1<<shift)) >> shift

        



    