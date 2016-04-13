from clrs import *
import random

def std(a):
    n_invers = 0
    for i in xrange(len(a) - 1):
        for j in xrange(i + 1, len(a)):
            if a[i] > a[j]:
                n_invers += 1
    return n_invers

@test
def _(f):
    for _ in xrange(1000):
        a = list(set(random.randint(0,100) for _ in xrange(100)))
        random.shuffle(a)
        oa = list(a)
        if f(a) != std(oa):
            raise Exception

@answer
def f(a):
    def merge(a, beg, mid, end):
        b = []
        i, j = beg, mid
        n_invers = 0
        k = beg
        while i < mid and j < end:
            if a[i] <= a[j]:
                b.append(a[i])
                i += 1
            else:
                b.append(a[j])
                j += 1
                if i < mid:
                    n_invers += mid - i
            k += 1
        b += a[i:mid] + a[j:end]
        a[beg:end] = b
        return n_invers
    n = len(a)
    run_len = 1
    n_invers = 0
    while run_len < n:
        for i in xrange(0, n, 2 * run_len):
            n_invers += merge(
                a, i, min(n, i + run_len), min(n, i + 2 * run_len))
        run_len *= 2
    return n_invers
