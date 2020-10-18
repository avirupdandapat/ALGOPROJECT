from array import array


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


def merge_sort(a):
    if len(a) == 0: return
    aux = [None for i in range(len(a))]
    _sort(a, aux, lo=0, hi=len(a) - 1)
    return a


def _sort(a, aux, lo, hi):
    if hi <= lo: return
    mid = int(lo + (hi - lo) / 2)
    _sort(a, aux, lo, mid)
    _sort(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)


def merge(a, aux, lo, mid, hi):
    assert isSorted(a, lo, mid)
    assert isSorted(a, mid + 1, hi)

    aux = a
    i = lo
    j = mid+1
    for k in range(0, len(a)):
        if less(a[i], a[j]):
            aux[k] = a[i]
            i += 1
        elif less(a[j], a[i]):
            aux[k] = a[j]
            j += 1
        elif i > mid + 1:
            aux[k] = a[j]
            j += 1
        elif j > hi:
            aux[k] = a[i]
            i += 1

    # return aux


b = [8, 2, 6, 45, 0, 7, 34, 61, 23, 72, 19, 103, 39, 84, 12]
# arr1 = selection_sort(b)
arr1 = merge_sort(b)
print(arr1)
assert isSorted(arr1)
