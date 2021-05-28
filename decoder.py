
from bitarray import bitarray


class Decoder:
    def __init__(self):
        pass

    def decode(self, array):
        decoded_array = bitarray(len(array) // 3)
        for i in range(0, len(array), 3):
            one_counter = array[i] + \
                array[i+1] + array[i+2]

            if(one_counter >= 2):
                decoded_array[i//3] = 1
            else:
                decoded_array[i//3] = 0

        return decoded_array
