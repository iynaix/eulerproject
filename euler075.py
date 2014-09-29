import math


def euler75():
    #start generating pythogarean triples via euclid's algorithm
    start = 1500000
    for m in range(1, int(math.sqrt(start))):
        for n in range(1, m):
            print m * m - n * n, 2 * m * n, m * m + n * n
