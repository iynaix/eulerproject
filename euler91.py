import itertools

def num_triangles(n):
    ret = 0
    rng = range(n + 1)
    for x1, y1, x2, y2 in itertools.product(rng, rng, rng, rng):
        if x1 == x2 or y1 == y2:
            continue
        if x1 * y2 - x2 * y1:
            ret += 1
    return ret

print num_triangles(1)
print num_triangles(2)
print num_triangles(3)
