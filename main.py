from generator import Generator
from coder import Coder


def main():
    generator = Generator(10)
    print(generator.bit_array)
    print(len(generator.bit_array))
    coder = Coder(generator.bit_array)
    print(coder.triple_array)
    print(coder.length)


if __name__ == '__main__':
    main()
