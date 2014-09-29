import itertools


def euler59():
    with open("cipher1.txt", "rU") as fp:
        msg = [int(c) for c in fp.read().strip().split(",")]

    final_msg = ""
    max_spaces = 0

    space = ord(" ")
    char_rng = range(ord("a"), ord("a") + 26)
    for passwd in itertools.product(char_rng, char_rng, char_rng):
        decoded = [a ^ b for a, b in
                   itertools.izip(msg, itertools.cycle(passwd))]

        #number of spaces
        spaces = decoded.count(space)
        if spaces > max_spaces:
            max_spaces = spaces
            final_msg = decoded

    return sum(final_msg)
