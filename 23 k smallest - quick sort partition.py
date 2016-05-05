from clrs import *
import random

@check
def _(f):
    #random.seed(0)
    a, sa = case.sa()
    oa = list(a)
    k = random.randint(0, len(a) - 1)
    rans = sa[k]
    ans = f(a, k)
    yield ans == rans
    print ans, rans, oa, sa, k

@answer
def f(a, k):
    b, e = 0, len(a)
    while True:
        i = random.randint(b, e - 1)
        a[b], a[i] = a[i], a[b]
        m = b + 1
        for i in xrange(m, e):
            if a[i] < a[b]:
                a[m], a[i] = a[i], a[m]
                m += 1
        m -= 1
        a[b], a[m] = a[m], a[b]
        if k < m:
            e = m
        elif m < k:
            b = m + 1
        else:
            return a[m]
assert f([1], 0) == 1

u'''
worst case O(n^2)
but with this optimization
the array with all same element will be O(n)
while without it's O(n^2)
------------- below is wrong conclusion
well, this is not needed
cause qsort has two recursive call
but this has only one
so even with the degenerated case it's still O(n)
'''
@answer
def _(a, k):
    b, e = 0, len(a)
    while True:
        i = random.randint(b, e - 1)
        a[b], a[i] = a[i], a[b]
        l = b + 1
        r = e
        i = b + 1
        while i < r:
            if a[i] < a[b]:
                a[l], a[i] = a[i], a[l]
                l += 1
                i += 1
            elif a[b] < a[i]:
                r -= 1
                a[r], a[i] = a[i], a[r]
            else:
                i += 1
        l -= 1
        a[l], a[b] = a[b], a[l]
        if k < l:
            e = l
        elif r <= k:
            b = r
        else:
            return a[l]
