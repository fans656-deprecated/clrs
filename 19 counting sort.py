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

########################################
u'''
https://en.wikipedia.org/wiki/Counting_sort
c中存储 < c[i] 的元素个数
最后从前往后放置，比CLRS里的写起来更自然点
'''

@check
def _(f):
    a, rans = case.sa()
    yield f(a) == rans

@answer
def counting_sort(a):
    mi, ma = min(a), max(a)
    k = ma - mi + 1
    b = list(a)
    a, b = b, a
    c = [0] * k
    for t in a:
        c[t - mi] += 1
    tot = 0
    for i in xrange(k):
        t = c[i]
        c[i] = tot
        tot += t
    for t in a:
        b[c[t - mi]] = t
        c[t - mi] += 1
    return b
