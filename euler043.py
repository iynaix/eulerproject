import itertools
from utils import from_digits


def euler43():
    ret = []
    for arr in itertools.permutations(range(10), 10):
        if arr[0] == 0:
            continue
        if from_digits(arr[1:4]) % 2:
            continue
        if from_digits(arr[2:5]) % 3:
            continue
        if from_digits(arr[3:6]) % 5:
            continue
        if from_digits(arr[4:7]) % 7:
            continue
        if from_digits(arr[5:8]) % 11:
            continue
        if from_digits(arr[6:9]) % 13:
            continue
        if from_digits(arr[7:10]) % 17:
            continue
        ret.append(from_digits(arr))
    return sum(ret)
