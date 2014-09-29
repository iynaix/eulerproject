from utils import is_square


def gen_integral_almost_equilateral_triangles(max_x, limit):
    for x in range(2, max_x):
        a = 4 * x * x * x * x - (2 * x * x - (x - 1) * (x - 1)) * \
                                (2 * x * x - (x - 1) * (x - 1))
        if a % 16 == 0:
            if is_square(a / 16):
                perimeter = 3 * x - 1
                if perimeter <= limit:
                    yield perimeter

        a = 4 * x * x * x * x - (2 * x * x - (x + 1) * (x + 1)) * \
                                (2 * x * x - (x + 1) * (x + 1))
        if a % 16 == 0:
            if is_square(a / 16):
                perimeter = 3 * x + 1
                if perimeter <= limit:
                    yield perimeter


def euler94():
    # solve x + x + x - 1 = 1000000000
    limit = 10 ** 9
    max_x = (limit + 1) // 3
    return sum(a for a in
               gen_integral_almost_equilateral_triangles(max_x, limit))
