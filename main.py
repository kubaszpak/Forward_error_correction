import time
import matplotlib.pyplot as plt
from decoder import Decoder
from channel import Channel
from coder import Coder
from generator import Generator
from bitarray.util import urandom
from bitarray import bitarray
import bchlib
import os


def error_factor(generated_array, decoded_array):
    if(len(generated_array) != len(decoded_array)):
        return None
    error_counter = 0
    for i in range(len(generated_array)):
        if(generated_array[i] != decoded_array[i]):
            error_counter += 1

    return error_counter/len(generated_array)*100


def main():
    # start = time.time()

    # a = []
    # b = []

    # for i in range(10, 25):

    # generator = Generator(2**20)
    # # print(generator.bit_array)

    # coder = Coder(generator.bit_array)

    # # a.append(i)

    # channel = Channel(coder.triple_array, 0.15)
    # # print(coder.triple_array)

    # decoder = Decoder(channel.distorted_array)
    # # print(decoder.decoded_array)

    # print(error_factor(generator.bit_array, decoder.decoded_array))

    # print(a, b)
    # plt.plot(a, b)
    # plt.title("Error percentage depending on the sample size m")
    # plt.xlabel("Sample size m as Exponent of two")
    # plt.ylabel("Error factor in %")
    # plt.show()
    # end = time.time()
    # print(end-start)

    """ETAP II"""

    # data = bitarray(800000)  # random bitarray len = 512
    # data = bytearray(os.urandom(512))

    # create a bch object
    BCH_POLYNOMIAL = 8219
    BCH_BITS = 32
    bch = bchlib.BCH(BCH_POLYNOMIAL, BCH_BITS)

    ecc = bch.encode(data)

    print(ecc)

    result_bits = bitarray()

    result_bits.frombytes(bytes(ecc))

    print(len(data))
    print(len(result_bits))
    print(error_factor(data, result_bits))


if __name__ == '__main__':
    main()
