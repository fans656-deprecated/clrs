from clrs import *
import random

@check
def _(f):
    a, rans = case.sa()
    yield f(a) == rans

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
            k = beg + 1
            for i in xrange(beg + 1, end):
                if a[i] < a[beg]:
                    a[k], a[i] = a[i], a[k]
                    k += 1
            a[k - 1], a[beg] = a[beg], a[k - 1]
            sort(a, beg, k - 1)
            sort(a, k, end)
    sort(a, 0, len(a))
    return a

@answer
def f(a):
    def sort(a, beg, end):
        if end - beg > 1:
            k = beg
            for i in xrange(beg, end - 1):
                if a[i] < a[end - 1]:
                    a[i], a[k] = a[k], a[i]
                    k += 1
            a[k], a[end - 1] = a[end - 1], a[k]
            sort(a, beg, k)
            sort(a, k + 1, end)
    sort(a, 0, len(a))
    return a
