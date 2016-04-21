# coding: utf-8
from clrs import *
import random

# 写复杂点的原因是要求stable
def counting_sort(a, lo, hi):
    m = hi - lo + 1
    b = list(a)
    c = [0] * m
    for t in a:
        c[t - lo] += 1
    for i in xrange(1, m):
        c[i] += c[i - 1]
    for i in xrange(len(a) - 1, -1, -1):
        b[c[a[i] - lo] - 1] = a[i]
        c[a[i] - lo] -= 1
    a[:] = b
    return a

@check
def _():
    a, rans = case.sa()
    lo, hi = min(a), max(a)
    yield counting_sort(a, lo, hi) == rans

########################################
# 8.2-4 p197
def preprocess(a, lo, hi):
    m = hi - lo + 1
    c = [0] * m
    for t in a:
        c[t - lo] += 1
    for i in xrange(1, m):
        c[i] += c[i - 1]
    return [0] + c

def count(c, b, e, lo):
    return c[e - lo + 1] - c[b - lo]

def std(a, b, e):
    return len([t for t in a if b <= t <= e])

a = case.a()
lo, hi = min(a), max(a)
c = preprocess(a, lo, hi)
@check
def _():
    b, e = random.randint(lo, hi), random.randint(lo, hi)
    if b > e:
        b, e = e, b
    ans = count(c, b, e, lo)
    rans = std(a, b, e)
    yield ans == rans
