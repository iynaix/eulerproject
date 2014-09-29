def euler231():
    #nCk = n! / (k! * (n-k)!)
    n = 20000000
    k = 15000000

    upper = range(k + 1, n + 1)
    lower = range(1, n - k + 1)
    print upper
    print lower

    return factors_C(n, k)
