from bitarray import bitarray


class Coder:
    def __init__(self):
        pass

    def triple_code(self, array):
        _len = len(array) * 3
        tripple_array = bitarray(_len)

        # tripple_array = bitarray([array[i//3] for i in range(0, _len, 3) for _ in range(3)])

        for i in range(0, _len, 3):
            for j in range(3):
                tripple_array[i+j] = array[i//3]
        return tripple_array
