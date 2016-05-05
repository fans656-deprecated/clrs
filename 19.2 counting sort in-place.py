# coding: utf-8
from clrs import *
import random

u'''
http://stackoverflow.com/questions/15682100/sorting-in-linear-time-and-in-place
这里讨论了好几种方法，并没仔细看
以下的第一种方法是自己独立想出来的
'''

def counting_sort(a):

    def hist(a, mi, k):
        c = [0] * k
        for t in a:
            c[t - mi] += 1
        return c

    def prefix_sum(a):
        for i in xrange(1, len(a)):
            a[i] += a[i - 1]
        return a

    def next_abnormality(i):
        end = ends[i]
        idx = idxs[i]
        while idx < end and a[idx] - mi == i:
            idx += 1
        idxs[i] = idx
        return idx

    mi, ma = min(a), max(a)
    k = ma - mi + 1
    ends = prefix_sum(hist(a, mi, k))
    idxs = [0] + ends[:-1]
    for i in xrange(k):
        next_abnormality(i)
    for i in xrange(k):
        idx = idxs[i]
        end = ends[i]
        while idx < end:
            j = a[idx] - mi
            idx_p = idxs[j]
            a[idx], a[idx_p] = a[idx_p], a[idx]
            next_abnormality(j)
            if a[idx] - mi == i:
                idx = next_abnormality(i)
    return a

@check
def _():
    a, rans = case.sa(simple=True)
    ans = counting_sort(a)
    yield ans == rans
