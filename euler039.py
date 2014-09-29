def euler39():
    #a+b > c if not it wont be a triangle
    #c <= 500 because of the above constraint
    #brute force using a hash table
    res = {}
    for a in range(1, 501):
        for b in range(1, 501):
            for c in range(1, 501):
                s = a + b + c
                if s <= 1000 and a * a + b * b == c * c:
                    try:
                        res[s] += 1
                    except KeyError:
                        res[s] = 1
    return max(res.items(), key=lambda x: x[1])[0]
