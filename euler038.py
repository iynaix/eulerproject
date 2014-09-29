from utils import is_pandigital


def euler38():
    res = {"pandigital": 0, "n": 0}
    for n in xrange(2, 99999999):
        all_str = str(n)
        if all_str[0] == "9":
            for i in xrange(2, 10):
                if len(all_str) >= 9:
                    break
                all_str += str(n * i)
        #pandigital check
        if len(all_str) == 9:
            all_str = int(all_str)
            if is_pandigital(all_str):
                if int(all_str) > res["pandigital"]:
                    res = {"pandigital": all_str, "n": n}
    return res["pandigital"]
