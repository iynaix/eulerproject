import math
from itertools import combinations
from collections import defaultdict


def gen_power_list(digit_length):
    lower = int(math.sqrt(10 ** digit_length))
    upper = int(math.sqrt(10 ** (digit_length + 1)))
    for x in range(lower, upper + 1):
        yield x * x


def euler98():
    words = open("words.txt").read().replace('"', '').split(",")

    anagrams_dict = defaultdict(list)
    for word in words:
        anagrams_dict[''.join(sorted(word))].append(word)

    anagrams = [v for v in anagrams_dict.values() if len(v) > 1]
    anagrams = sorted(anagrams, key=lambda x: (len(x[0]), x), reverse=True)

    power_lists = defaultdict(set)
    for x in range(1, int(math.sqrt(10 ** len(str(anagrams[0][0])))) + 1):
        x = str(x * x)
        power_lists[len(x)].add(x)

    ret = 0
    for anagram in anagrams:
        power_list = power_lists[len(anagram[0])]
        for a1, a2 in combinations(anagram, 2):
            for p in power_list:
                anagram_set_len = len(set(str(a1)))
                if anagram_set_len != len(set(p)):
                    continue
                mapping_dict = dict(zip(str(a1), p))
                mapped = ''.join(mapping_dict[c] for c in str(a2))
                if mapped in power_list:
                    ret = max(ret, int(p), int(mapped))
    return ret
