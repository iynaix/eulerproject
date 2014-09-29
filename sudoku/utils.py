def intersection(*args):
    """
    returns a set of the intersection of all the given iterables
    """
    if not args:
        return set()

    ret = set(args[0])
    for x in args[1:]:
        ret = ret.intersection(x)
    return ret
