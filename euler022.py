def euler22():
    arr = sorted(open("names22.txt").read().replace('"', '').split(","))
    ret = 0
    for i, s in enumerate(arr):
        ret += sum([ord(c) - ord("A") + 1 for c in s]) * (i + 1)
    return ret
