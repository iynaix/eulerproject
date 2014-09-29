def euler6():
    return sum(range(1, 101)) ** 2 - sum([i * i for i in range(1, 101)])
