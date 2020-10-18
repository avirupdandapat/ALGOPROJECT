from array import array


def less(v, w):
    if v is None or w is None: return False
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
        if less(a[i], a[i - 1]):
            return False
    return True


def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if less(arr[j], arr[min]):
                min = j
        exch(arr, i, min)

    return arr


def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i, 0, -1):
            if less(arr[j], arr[j - 1]):
                exch(arr, j, j - 1)
            else:
                break

    return arr


# Merge Sort
def merge_sort(a):
    if len(a) == 0: return
    aux = array('i', range(len(a)))  # [None for i in range(len(a))]
    _sort(a, aux, 0, len(a) - 1)
    # _sort(a, aux, 0, len(a) - 1)
    # _sort(a, aux, 0, len(a) - 1)
    return a


def _sort(a, aux, lo, hi):
    if hi <= lo: return
    mid = int(lo + (hi - lo) / 2)
    _sort(a, aux, lo, mid)
    _sort(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)
    # return aux


def merge(a, aux, lo, mid, hi):
    # assert isSorted(a, lo, mid)
    # assert isSorted(a, mid + 1, hi)

    # aux[lo:hi + 1] = a[lo:hi + 1]
    for it in range(lo, hi + 1):
        aux[it] = a[it]
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        # print(lo, i, j, hi)
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif less(a[j], a[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1
    # print(lo, i, j, hi)


# Quick Sort
def _partition(a, lo, hi):
    i = lo
    j = hi + 1
    while True:
        i += 1
        while less(a[i], a[lo]):
            if i == hi: break
            i += 1
        j -= 1
        while less(a[lo], a[j]):
            if j == lo: break
            j -= 1

        if i >= j: break
        exch(a, i, j)

    exch(a, lo, j)
    return j


def _qsort(a, lo, hi):
    if hi <= lo: return
    j = _partition(a, lo, hi)
    _qsort(a, lo, j - 1)
    _qsort(a, j + 1, hi)
    # return aux


def Quick_sort(a):
    _qsort(a, 0, len(a) - 1)
    return a


b = [8, 2, 6, 45, 0, 7, 34, 61, 23, 72, 19, 103, 2,  39, 84, 12, 13]
# b = [5, 4, 3, 2]
# c = selection_sort(b)
# c = merge_sort(b)
# print(c)
# assert isSorted(c)


print(Quick_sort(b))
