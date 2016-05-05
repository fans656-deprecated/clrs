# coding: utf-8
from clrs import *
import random

# 8-2 p206

@check
def _(f):
    a, rans = case.sa((0,1))
    yield f(a) == rans

@answer
def counting_sort(a):
    p = 0
    q = a.count(0)
    b = list(a)
    for t in b:
        if t == 0:
            a[p] = t
            p += 1
        else:
            a[q] = t
            q += 1
    return a
