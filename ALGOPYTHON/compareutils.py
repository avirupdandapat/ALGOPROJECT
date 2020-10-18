def less(v, w):
    return v < w


def exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap


def isSorted(a, lo=None, hi=None):
    if lo is None and hi is None:
        lo = 0
        hi = len(a) - 1

    for i in range(lo + 1, hi + 1):
        if less(a[i], a[i + 1]):
            return False
    return True


