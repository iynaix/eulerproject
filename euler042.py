from utils import is_triangular


def euler42():
    ret = 0
    for word in open("words42.txt").read().replace('"', "").split(","):
        ret += is_triangular(sum([ord(c) - ord("A") + 1 for c in word]))
    return ret
