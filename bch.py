import numpy as np
from komm import BCHCode
from channel import Channel



class BCH:

    def __init__(self):
        pass

    # μ - m - Indicates the length of the codeword n = 2^(μ) - 1
    # τ - t - The parameter τ is called the designed error-correcting capability of the BCH code (zdolność korekcyjna)
    # dimension k
    def code(data_array, m, t, k, p):

        code = BCHCode(m, t)
        entire_decoded_message = []

        counter = 0
        for i in range(0, len(data_array), k):
            counter += 1
            incomplete_array = []
            if(i + k >= len(data_array)):
                
                for j in range(i, i + k):
                    if(j < len(data_array)):
                        incomplete_array.append(data_array[j])
                    else:
                        incomplete_array.append(0)

                np_packet = np.array(incomplete_array)
                # print(counter,np_packet)
            else:
                np_packet = np.array([data_array[j] for j in range(i, i + k)])  # tablica int
                # print(counter,np_packet)
                
            

            # print("Length n, dimension k, min distance of BCHCode:",
            #     (code.length, code.dimension, code.minimum_distance))

            # print(code.generator_polynomial) # 0b1000111110101111

            encoded_msg = code.encode(np_packet)

            distorted_msg = Channel(p).distort(encoded_msg)

            decoded_msg = code.decode(distorted_msg)

            # received_msg = code.message_from_codeword(distorted_msg)

            # print("Encoded msg:   ", encoded_msg)

            # print("Distorted msg: ", distorted_msg)

            # print("Decoded msg:   ", decoded_msg)

            # print("Received msg:  ", received_msg)

            entire_decoded_message += decoded_msg.tolist()

        return entire_decoded_message
            

