from clrs import *
import random

@test
def _(f):
    for _ in xrange(100):
        a = [i for i in xrange(100)]
        v = random.randint(0, 99)
        i = f(a, v)
        if i != a.index(v):
            raise Exception
    if 0 <= f(a, -1) < len(a):
        raise Exception

@answer
def f(a, v):
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
