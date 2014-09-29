from sympy.matrices import Matrix


def euler101():
    #actual function that generates polynomials
    def u(n):
        return n ** 3

    order = 3  # largest polynomial order of u
    seq = [u(x) for x in range(1, order + 2)]
    A = Matrix([[1 ** 1, 1], [8 ** 1, 1]][::-1])
    b = Matrix([[x] for x in seq[:2]])
    return A.inv() * b
