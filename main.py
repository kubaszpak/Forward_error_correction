import time
import matplotlib.pyplot as plt
from decoder import Decoder
from channel import Channel
from coder import Coder
from generator import Generator
import os
import random


def error_factor(generated_array, decoded_array):
    if(len(generated_array) != len(decoded_array)):
        return None
    error_counter = 0
    for i in range(len(generated_array)):
        if(generated_array[i] != decoded_array[i]):
            error_counter += 1

    return error_counter/len(generated_array)*100


def main():
    start = time.time()

    # a = []
    # b = []

    # for i in range(0, 30):

    generated_array = Generator().populate_array(2**20)
    # print(generated_array)

    coded_array = Coder().triple_code(generated_array)
    # print(coded_array)

    # a.append(i / 100)

    distorted_array = Channel(i/100).distort(coded_array)
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

    


if __name__ == '__main__':
    main()
