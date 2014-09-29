import decimal
import math
from utils import is_int, digits


def euler80():
    decimal.getcontext().prec = 105

    ret = 0
    for i in range(2, 101):
        if is_int(math.sqrt(i)):
            continue
        x = str(decimal.Decimal(i).sqrt()).replace(".", "")
        ret += sum(digits(x[:100]))
    return ret
