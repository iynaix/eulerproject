def euler145():
    def is_reversible(x):
        if x % 10 == 0:
            return False
        for c in str(x + int(str(x)[::-1])):
            if c == "0" or c == "2" or c == "4" or c == "6" or c == "8":
                return False
        return True

    #there are no 1 or 5 or 9 digit reversible numbers
    #http://bit.ly/ZluRYr
    ret = 0
    for n in xrange(11, 10 ** 8):
        ret += is_reversible(n)
    return ret
