import itertools


def euler89():
    with open("roman89.txt", "rU") as fp:
        lines = fp.read().splitlines()

    tbl = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
    }
    numerals = sorted(tbl.items(), reverse=True, key=lambda x: x[1])

    def int_to_roman(n):
        roman = []
        for ltr, num in numerals:
            k, n = divmod(n, num)
            roman.append(ltr * k)
        return "".join(roman)

    def roman_to_int(num):
        x = [tbl[c] for c in num]
        #compress ranges of items of the same length
        x = [sum(v) for k, v in itertools.groupby(x)]
        ret = 0
        for idx in range(len(x) - 1):
            if x[idx] < x[idx + 1]:
                ret -= x[idx]
            else:
                ret += x[idx]
        #handle last element
        return ret + x[-1]

    ret = 0
    for num in lines:
        ret += len(num) - len(int_to_roman(roman_to_int(num)))
    return ret
