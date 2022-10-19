import collections
import math
from operator import itemgetter


def analyze_file(filename, char_size):
    with open(filename, "rb") as file:
        file_data = []
        some_char = file.read(char_size)
        while some_char != b"":
            file_data.append(some_char)
            some_char = file.read(char_size)
        n = len(file_data)
        v = collections.Counter(file_data)
        sum_info = 0
        res = []
        for i in sorted(v):
            res.append([i, v[i], v[i] / n, math.ceil(-math.log2(v[i] / n))])
            sum_info += math.ceil(-math.log2(v[i] / n))
        print('-' * 40)
        print('Sorted alphabetically')
        print('-' * 40)
        for i in sorted(res):
            print("Char: %#6x n = %6d v = %f I = %2d" % (int.from_bytes(i[0], "big"), i[1], i[2], i[3]))

        print('-' * 40)
        print('Sorted by frequency')
        print('-' * 40)
        for i in (sorted(res, key=itemgetter(2))):
            print("Char: %#6x n = %6d v = %f I = %2d" % (int.from_bytes(i[0], "big"), i[1], i[2], i[3]))
        print('-' * 40)
        print("Summary:")
        print("Size:", n, "chars")
        print("Info:\n\tBit: ", sum_info, "\n\tByte: ", math.ceil(sum_info / 8))


analyze_file("some_text .txt", 1)
analyze_file("some_text .txt", 2)