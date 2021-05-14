import time
import matplotlib.pyplot as plt
from decoder import Decoder
from channel import Channel
from coder import Coder
from generator import Generator
import random
from bitarray import bitarray
import bitarray.util as b_util
from komm import BCHCode
import numpy as np


def error_factor(generated_array, decoded_array):
    if(len(generated_array) != len(decoded_array)):
        return None
    error_counter = 0
    for i in range(len(generated_array)):
        if(generated_array[i] != decoded_array[i]):
            error_counter += 1

    return error_counter/len(generated_array)*100


def how_many_distortions(generated_array, decoded_array):
    if(len(generated_array) != len(decoded_array)):
        return None
    error_counter = 0
    for i in range(len(generated_array)):
        if(generated_array[i] != decoded_array[i]):
            error_counter += 1

    return error_counter


def main():
    start = time.time()

    # a = []
    # b = []

    # for i in range(0, 30):

    generated_array = Generator().populate_array(2**18)
    # print(generated_array)

    coded_array = Coder().triple_code(generated_array)
    # print(coded_array)

    # a.append(i / 100)
    # distorted_array = Channel(i/100).distort(coded_array)

    distorted_array = Channel(0.15).distort(coded_array)
    # print(distorted_array)

    decoded_array = Decoder().decode(distorted_array)
    # print(decoded_array)

    print(error_factor(generated_array, decoded_array))
    # b.append(error_factor(generated_array, decoded_array))

    # print(a, b)
    # plt.plot(a, b)
    # plt.title("Error percentage depending on the probability p")
    # plt.xlabel("Probability of error p")
    # plt.ylabel("Error factor in %")
    # plt.show()
    end = time.time()
    print("Time:", end-start)

    """
    Etap II
    """
    print("Stage 2")

    example_bit_array = b_util.urandom(121)

    np_array = np.array([example_bit_array[i]
                        for i in range(len(example_bit_array))])  # tablica int

    # μ - m - Indicates the length of the codeword n = 2^(μ) - 1
    m = 9
    # τ - t - The parameter τ is called the designed error-correcting capability of the BCH code (zdolność korekcyjna)
    t = 58
    # dimension k = 123

    code = BCHCode(m, t)

    print("Length n, dimension k, min distance of BCHCode:",
          (code.length, code.dimension, code.minimum_distance))

    # print(code.generator_polynomial) # 0b1000111110101111

    encoded_msg = code.encode(np_array)

    distorted_msg = Channel(0.4).distort(encoded_msg)

    decoded_msg = code.decode(distorted_msg)

    received_msg = code.message_from_codeword(distorted_msg)

    print("Encoded msg:   ", encoded_msg)

    print("Distorted msg: ", distorted_msg)

    print("Decoded msg:   ", decoded_msg)

    print("Received msg:  ", received_msg)

    print("Input np array:", np_array, "Length:", len(np_array))

    print("Error [%] - decoded msg: ", error_factor(np_array, decoded_msg))

    print("Distorted bits/ All bits: ",
          how_many_distortions(encoded_msg, distorted_msg), "/", len(encoded_msg))

    print("Error bits/ All bits: ",
          how_many_distortions(np_array, decoded_msg), "/", len(np_array))

    # print("Error [%] - received msg:", error_factor(np_array, received_msg))


if __name__ == '__main__':
    main()
