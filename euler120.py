def euler120():
    """
    for even n, (a+1)^n + (a-1)^n = 2a^n+2
    for odd n, (a+1)^n + (a-1)^n = 2a^n+2an

    Dividing by a^2, the remainders are therefore 2 for even n and 2an for
    odd n
    For odd n, 2an < a^2
    """
    return sum([2 * a * ((a - 1) // 2) for a in range(3, 1001)])
