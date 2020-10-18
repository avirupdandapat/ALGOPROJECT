from array import array

ID = array('i', range(10))
ID[5] = 7
ld = [5]
# for i, curr_ID in enumerate(ID):
# print(ID[i])
# print(curr_ID)

for s in ID:
    print(ID[s])


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


for i in range(5, 0, -1):
    print(i)

b = [8, 2, 6, 45, 0, 7, 34, 61, 23, 72, 19, 103, 39, 84, 12]



