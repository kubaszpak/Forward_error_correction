from PIL import Image
import io
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
from bch import BCH
from bch_params import bch_code_parameters
import sys
np.set_printoptions(threshold=sys.maxsize)


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


def fill_with_zeros(array, n):
    filled_array = array.copy()
    for i in range(n-len(array)):
        filled_array.append(0)
    return filled_array


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
    # 2048

    bch = BCH()

    a = []
    b = []
    error = 0

    sent_msg = b_util.urandom(512)

    m = 8
    t = 63
    k = 9

    # 7_21_29

    # received_msg = BCH.code(sent_msg, m, t, k, 0.3)

    # for i in range(0, 20, 1):
    #     for j in range(10):
    #         received_msg = BCH.code(sent_msg, 3, 1, 4, i/100)

    #         filled_array = fill_with_zeros(sent_msg, len(received_msg))

    #         # print(len(example_bit_array), len(received_msg))
    #         # # print(received_msg)
    #         # print("Error [%] - decoded msg: ", error_factor(example_bit_array, received_msg))
    #         error += error_factor(filled_array, received_msg)
    #     error /= 10
    #     a.append(i/100)
    #     b.append(error)

    # print(a, b)
    # plt.plot(a, b)

    # plt.title(
    #     f"Error percentage depending on the probability p \nfor m = {m} k = {k} t = {t}")
    # plt.xlabel("Probability of error p")
    # plt.ylabel("Error factor in %")
    # plt.show()

    for i in range(0,20,3):
        counter = 0
        for m in bch_code_parameters:
            for t in bch_code_parameters[m]:
                counter +=1

                received_msg = BCH.code(sent_msg, m, t, bch_code_parameters[m][t], i/100)


                filled_array = fill_with_zeros(sent_msg, len(received_msg))
                # print(len(example_bit_array), len(received_msg))
                # # print(received_msg)
                # print("Error [%] - decoded msg: ", error_factor(example_bit_array, received_msg))
                error += error_factor(filled_array, received_msg)
        a.append(i/100)
        b.append(error/counter)
        error = 0
        print(counter)
    print(a, b)
    plt.plot(a, b)
    plt.title("Error percentage depending on the probability p")
    plt.xlabel("Probability of error p")
    plt.ylabel("Error factor in %")
    plt.show()
if __name__ == '__main__':
    main()

# print("Input np array:", np_array, "Length:", len(np_array))

# print("Error [%] - decoded msg: ", error_factor(np_array, decoded_msg))

# print("Distorted bits/ All bits: ",
#     how_many_distortions(encoded_msg, distorted_msg), "/", len(encoded_msg))

# print("Error bits/ All bits: ",
#     how_many_distortions(np_array, decoded_msg), "/", len(np_array))

# print("Error [%] - received msg:", error_factor(np_array, received_msg))
