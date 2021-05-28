import numpy as np


class BCH:

    def __init__(self):
        pass

    def code(self, data_array, m, t, k):
        # for(int i = 0; i < len(data_array); i+=k)
        # 512
        # 0 131 262 393 524
        # 0-127, 128-255, 256-383,384-511,512
        # i, i + k - 1

        for i in range(0, len(data_array), k):

            if(i + k >= len(data_array)):
                incomplete_array = []
                for j in range(i, i+k):
                    if(i < len(data_array)):
                        incomplete_array[j-i] = data_array[j]
                    else:
                        incomplete_array[j-i] = 0

                    np_packet = np.array([data_array[j]
                                          for j in range(i, len(data_array))])

                break
            else:
                np_packet = np.array([data_array[j]
                                      for j in range(i, i + k)])  # tablica int
