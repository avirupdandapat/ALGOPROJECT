def _less(v, w): return v < w


# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap


# **********************************************************************
#  Check if array is sorted - useful for debugging
# **********************************************************************/
def _isSorted(a, lo=None, hi=None):
    if lo is None and hi is None:
        lo = 0
        hi = len(a)
    for i in range(lo + 1, hi + 1):
        if _less(a[i], a[i - 1]): return False
    return True


def Sort(a):
    # _add_history(array_history, a)  # Record initial state of array
    # random.shuffle(a)  # Needed to ensure performance will be good. 05:56
    _sort(a, 0, len(a) - 1)


def _sort(a, lo, hi):
    """quicksort the subarray from a[lo] to a[hi]."""
    if hi <= lo: return;
    j = _partition(a, lo, hi)
    _sort(a, lo, j - 1)
    _sort(a, j + 1, hi)
    assert _isSorted(a, lo, hi)


def _partition(a, lo, hi):
    """partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]"""
    # and return the index j.
    i = lo
    j = hi + 1
    v = a[lo]
    while True:

        # find item on lo to swap
        i += 1
        while _less(a[i], v):
            if i == hi: break
            i += 1  # Increment i as long it is pointing to val < v

        # find item on hi to swap
        j -= 1
        while _less(v, a[j]):
            if j == lo: break  # redundant since a[lo] acts as sentinel
            j -= 1  # Decrement j as long as it is pointing to va > v

        # check if pointers cross
        if i >= j: break;
        # if array_history is not None: _add_history(array_history, a, (i, j))
        _exch(a, i, j)

    # put partitioning item v at a[j]
    # if array_history is not None: _add_history(array_history, a, (i, j))
    _exch(a, lo, j)
    # if array_history is not None: _add_history(array_history, a, (i, j))

    # now, a[lo .. j-1] <= a[j] <= a[j+1 .. hi]
    # j now points to partitioning element, after it has moved to its new spot
    return j


b = [8, 2, 6, 45, 0, 7, 34, 61, 23, 72, 19, 103, 39, 84, 12, 13]
print(Sort(b))
