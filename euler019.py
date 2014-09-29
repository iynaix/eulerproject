import datetime


def euler19():
    ret = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            ret += datetime.date(year, month, 1).weekday() == 6
    return ret
