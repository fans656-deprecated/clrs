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
    for i in xrange(1, len(a)):
        t = a[i]
        j = i - 1
        while j >= 0 and t < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
    return a

@answer
def _(a):
    for i, t in enumerate(a[1:]):
        while i >= 0 and t < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = t
    return a
