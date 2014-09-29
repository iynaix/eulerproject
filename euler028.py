def euler28():
    return sum((
        sum([1 - 4 * x + 4 * x * x for x in range(1, 502)]),
        sum([4 * x * x - 10 * x + 7 for x in range(1, 502)]),
        sum([4 * x * x - 8 * x + 5 for x in range(1, 502)]),
        sum([4 * x * x - 6 * x + 3 for x in range(1, 502)])
    )) - 3
