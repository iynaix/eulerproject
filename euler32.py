from utils import is_pandigital, multiplicands


def euler32():
    ret = 0
    #only up to 9999 because there won't be enough digits to go round
    for i in xrange(10, 10000):
        istr = str(i)
        #don't bother if there are digit repeats
        if len(set(istr)) != len(istr):
            continue

        for a, b in multiplicands(i):
            combined = "%s%s%s" % (a, b, i)
            if len(combined) == 9 and "0" not in combined and \
               is_pandigital(combined):
                ret += i
                break
    return ret
