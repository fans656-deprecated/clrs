from clrs import *
import random
from pprint import pprint

def gen():
    b = random.randint(2,10)
    a = [[random.randint(0,9) for _ in xrange(b)] for __ in xrange(100)]
    return a, b, sorted(list(a))

def bunchcard_sort(a, col, max_col):
    if len(a) > 1 and col < max_col:
        piles = [[] for _ in xrange(10)]
        for n in a:
            v = n[col]
            piles[v].append(n)
        del a[:]
        for pile in piles:
            a += bunchcard_sort(pile, col + 1, max_col)
    return a

@check
def _():
    a, b, rans = gen()
    ans = bunchcard_sort(a, 0, b)
    yield ans == rans

def counting_sort(a, idx):
    b = list(a)
    c = [0] * 10
    for n in a:
        v = n[idx]
        c[v] += 1
    for i in xrange(1, len(c)):
        c[i] += c[i - 1]
    for i in xrange(len(a) - 1, -1, -1):
        j = a[i][idx]
        c[j] -= 1
        b[c[j]] = a[i]
    a[:] = b

def radix_sort(a):
    d = len(a[0])
    for i in xrange(1, d + 1):
        counting_sort(a, -i)
    return a

@check
def _():
    a, b, rans = gen()
    ans = radix_sort(a)
    yield ans == rans

def reverse(a, b, e):
    e -= 1
    while b < e:
        a[b], a[e] = a[e], a[b]
        b += 1
        e -= 1
    return a

def shift(a, k):
    n = len(a)
    k = -k if k < 0 else n - k
    reverse(a, 0, k)
    reverse(a, k, n)
    reverse(a, 0, n)
    return a

def radix_sort(a):
    def counting_sort(a, idx):
        b = list(a)
        c = [0] * 256
        a, b = b, a
        for n in a:
            v = (n >> idx * 8) & 0xff
            c[v] += 1
        for i in xrange(1, len(c)):
            c[i] += c[i - 1]
        for i in xrange(len(a) - 1, -1, -1):
            n = a[i]
            v = (n >> idx * 8) & 0xff
            c[v] -= 1
            b[c[v]] = n
    for i in xrange(4):
        counting_sort(a, i)
    i = next(i for i in xrange(len(a)) if a[i] < 0)
    if i < len(a):
        shift(a, -i)
    return a

@check
def _():
    a, rans = case.sa()
    ans = radix_sort(a)
    yield ans == rans
    print ans, rans
