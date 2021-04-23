from generator import Generator
from coder import Coder
from channel import Channel
from decoder import Decoder
import matplotlib.pyplot as plt
import time


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
    generator = Generator(2**18)
    # print(generator.bit_array)

    coder = Coder(generator.bit_array)

    a = []
    b = []
    for i in range(30):

        a.append(i/100)

        channel = Channel(coder.triple_array, i/100)
        # print(coder.triple_array)

        decoder = Decoder(channel.distorted_array)
        # print(decoder.decoded_array)

        b.append(error_factor(generator.bit_array, decoder.decoded_array))

    print(a, b)
    plt.plot(a, b)
    plt.title("Error percentage depending on the probability of distortion p")
    plt.xlabel("Probability p")
    plt.ylabel("Error factor in %")
    plt.show()
    # end = time.time()
    # print(end-start)


if __name__ == '__main__':
    main()
