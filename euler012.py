from utils import polygonal_gen
from sympy import divisor_count


def euler12():
    for tri in polygonal_gen(3):
        if divisor_count(tri) > 500:
            return tri
