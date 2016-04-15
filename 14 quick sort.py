from clrs import *
import random

@check
def _(f):
    a, ans = case.sa()
    yield f(a), ans

@answer
def f(a):
    def sort(a, beg, end):
        if end - beg > 1:
            lim = beg + 1
            for i in xrange(beg + 1, end):
                if a[i] < a[beg]:
                    a[lim], a[i] = a[i], a[lim]
                    lim += 1
            a[beg], a[lim - 1] = a[lim - 1], a[beg]
            sort(a, beg, lim - 1)
            sort(a, lim, end)
    sort(a, 0, len(a))
    return a

@answer
def f(a):
    def sort(a, beg, end):
        if end - beg > 1:
            lim = beg
            for i in xrange(beg, end):
                if a[i] < a[end - 1]:
                    a[lim], a[i] = a[i], a[lim]
                    lim += 1
            a[lim], a[end - 1] = a[end - 1], a[lim]
            sort(a, beg, lim)
            sort(a, lim + 1, end)
    sort(a, 0, len(a))
    return a
