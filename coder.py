from bitarray import bitarray


class Coder:
    def __init__(self, array):
        self.length = len(array) * 3
        self.triple_array = bitarray(self.length)
        self.triple_code(array)

    def triple_code(self, array):
        for i in range(0, self.length, 3):
            self.triple_array[i] = array[i // 3]
            self.triple_array[i+1] = array[i // 3]
            self.triple_array[i+2] = array[i // 3]
