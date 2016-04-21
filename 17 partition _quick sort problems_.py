from clrs import *
import random

@check
def _(f):
    a = case.a()
    beg, end = f(a, 0, len(a))
    pivot = a[beg]
    yield (
        all(t < pivot for t in a[:beg]) and
        all(t > pivot for t in a[end:]) and
        all(t == pivot for t in a[beg:end])
    )
    print a, beg, end

@answer
def partition(a, beg, end):
    pivot = a[beg]
    l = beg
    r = end
    m = l + 1
    i = m
    while i < r:
        if a[i] < pivot:
            a[i], a[l] = a[l], a[i]
            l += 1
            m += 1
            i += 1
        elif a[i] > pivot:
            r -= 1
            a[i], a[r] = a[r], a[i]
        else:
            m += 1
            i += 1
    return l, r
