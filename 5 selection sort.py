from clrs import *
import random

@test
def _(f):
    for _ in xrange(100):
        a = [1,2,3,4,5]
        oa = list(a)
        random.shuffle(a)
        a = f(a)
        if a != [1,2,3,4,5]:
            raise Exception(
                'Expect {}, got {}'.format(oa, a)
            )

@answer
def _(a):
    for i in xrange(len(a) - 1):
        mi = i
        for j in xrange(i + 1, len(a)):
            if a[j] < a[mi]:
                mi = j
        if mi != i:
            t = a[mi]
            a[mi] = a[i]
            a[i] = t
    return a
