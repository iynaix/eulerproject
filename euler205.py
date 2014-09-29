import itertools
from collections import defaultdict


def euler205():
    def dice_expectation(num_dice, num_sides):
        dices = []
        for i in range(num_dice):
            dices.append(range(1, num_sides + 1))

        tbl = defaultdict(int)
        #simulate and tabulate rolling every combination of the dice
        for roll in itertools.product(*dices):
            tbl[sum(roll)] += 1

        #calculate E[x]
        sumprod = sum(total * count for total, count in tbl.iteritems())
        return sumprod * 1.0 / sum(tbl.values())

    print dice_expectation(9, 4)
    print dice_expectation(6, 6)
