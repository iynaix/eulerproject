def euler14():
    def collatz_len(n):
        l = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            l += 1
        return l

    longest_len = 0
    ret = 0
    for i in range(2, 1000000):
        l = collatz_len(i)
        if l > longest_len:
            longest_len = l
            ret = i
    return ret
