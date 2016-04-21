from clrs import *
import random

@check
def _(f):
    a, rans = case.sa()
    yield f(a) == rans

@answer
def f(a):
    left = lambda k: 2 * k + 1
    right = lambda k: 2 * k + 2
    parent = lambda k: (k - 1) // 2
    def heapify(a, i, end):
        while True:
            l = left(i)
            r = right(i)
            oi = i
            if l < end and a[l] > a[i]:
                i = l
            if r < end and a[r] > a[i]:
                i = r
            if i != oi:
                a[i], a[oi] = a[oi], a[i]
            else:
                return
    def make_heap(a):
        n = len(a)
        for i in xrange(parent(n - 1), -1, -1):
            heapify(a, i, n)
    make_heap(a)
    for end in xrange(len(a), 1, -1):
        end -= 1
        a[0], a[end] = a[end], a[0]
        heapify(a, 0, end)
    return a

@answer
def f(a):
    left = lambda k: 2 * k + 1
    right = lambda k: 2 * k + 2
    parent = lambda k: (k - 1) // 2
    def heapify(a, i, n):
        while True:
            l = left(i)
            r = right(i)
            oi = i
            if l < n and a[l] > a[i]:
                i = l
            if r < n and a[r] > a[i]:
                i = r
            if i != oi:
                a[i], a[oi] = a[oi], a[i]
            else:
                return
    def make_heap(a, n):
        for i in xrange(parent(n - 1), -1, -1):
            heapify(a, i, n)
    n = len(a)
    make_heap(a, n)
    while n:
        a[n - 1], a[0] = a[0], a[n - 1]
        n -= 1
        heapify(a, 0, n)
    return a
