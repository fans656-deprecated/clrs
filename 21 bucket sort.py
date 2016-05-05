# coding: utf-8
from clrs import *
import random

@check
def _(f):
    a, rans = case.sa()
    ans = f(a)
    yield ans == rans

def insertion_sort(a):
    for i in xrange(1, len(a)):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
    return a

@answer
def bucket_sort(a, n_buckets=5):
    mi, ma = min(a), max(a)
    k = ma - mi + 1
    m = (k + n_buckets - 1) // n_buckets
    buckets = [[] for _ in xrange(n_buckets)]
    for t in a:
        buckets[(t - mi) // m].append(t)
    a[:] = sum(buckets, [])
    return insertion_sort(a)

u'''
一个有趣的事是：当 n_buckets == 2 时，bucket_sort 原则上就变成了 quick_sort
因为 left bucket 的元素 < right bucket 的元素
'''

def bucket_sort(a, n_buckets=5):
    buckets = [[] for _ in xrange(n_buckets)]
    for t in a:
        buckets[int(t * n_buckets)].append(t)
    a[:] = sum(buckets, [])
    return insertion_sort(a)

@check
def _():
    a = [random.random() for _ in xrange(100)]
    oa = list(a)
    yield bucket_sort(a) == sorted(oa)
