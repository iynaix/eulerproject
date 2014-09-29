from sympy import n_order


def euler26():
    ret, max_period = 0, 0
    for i in range(3, 1000):
        try:
            res = n_order(10, i)
            if res > max_period:
                max_period = res
                ret = i
        except ValueError:
            pass
    return ret
