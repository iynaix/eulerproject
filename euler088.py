from sympy import factorint

def smallest_product_sum(k):
    n = 2
    while 1:
        total = 0
        total_cnt = 0
        for factor, cnt in factorint(n).iteritems():
            total += factor * cnt
            total_cnt += cnt
        print n, total_cnt, total, total + (k - total_cnt)
        if total + (k - total_cnt) == n:
            return n
        if n == 8:
            break
        n += 1

print smallest_product_sum(4)
