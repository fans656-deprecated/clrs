from clrs import *
import random

@check
def _(f):
    a, rans = case.sa()
    yield f(a) == rans

def partition(a, beg, end):
    i = random.randint(beg, end - 1)
    a[beg], a[i] = a[i], a[beg]
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
    return l, m

@answer
def _(a):
    def quick_sort(a, beg, end):
        while end - beg > 1:
            l, r = partition(a, beg, end)
            if l - beg < end - r:
                quick_sort(a, beg, l)
                beg = r
            else:
                quick_sort(a, r, end)
                end = l
        return a
    return quick_sort(a, 0, len(a))
