from utils import prod
import itertools

limit = 45
squares = [x * x for x in range(2, limit + 1)]

ret = 0
for n in range(2, limit + 1):
    for arr in itertools.combinations(squares, n):
        # ret += (sum(arr) == HALF)
        pass
print ret
