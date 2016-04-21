from clrs import *
import random

def binary_search(a, v):
    beg, end = 0, len(a)
    while beg < end:
        mid = (beg + end) // 2
        if a[mid] == v:
            return mid
        elif a[mid] < v:
            beg = mid + 1
        else:
            end = mid
    return -1

clrs.n_cases = 1
@check
def _():
    for _ in xrange(100):
        a = [i for i in xrange(100)]
        v = random.randint(0, 99)
        i = binary_search(a, v)
        assert i == a.index(v)
    assert not (0 <= binary_search(a, -1) < len(a))
    yield True
