from clrs import *
import random

def std(a, x):
    for t in a:
        for p in a:
            if t != p and x == t + p:
                return True
    return False

clrs.n_cases = 1
@check
def _(f):
    for _ in xrange(1000):
        a = set(random.randint(0,100) for _ in xrange(100))
        a = list(a)
        random.shuffle(a)
        x = random.randint(0,100) + random.randint(0,100)
        if f(a, x) != std(a, x):
            raise Exception
    x = 99999
    if f(a, x) != std(a, x):
        raise Exception
    yield True

def bsearch(a, t):
    beg, end = 0, len(a)
    while beg < end:
        mid = (beg + end) // 2
        if a[mid] == t:
            return True
        elif a[mid] < t:
            beg = mid + 1
        else:
            end = mid
    return False

@answer
def f(a, x):
    a.sort()
    for t in a:
        if x - t != t and bsearch(a, x - t):
            return True
    return False
