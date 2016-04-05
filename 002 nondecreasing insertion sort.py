from clrs import *

@test
def _(f):
    for _ in xrange(100):
        a = [1,2,3,4,5]
        oa = list(a)
        random.shuffle(a)
        a = f(a)
        if a != [5,4,3,2,1]:
            raise Exception(
                'Expect {}, got {}'.format(oa, a)
            )

@answer
def _(a):
    for i, t in enumerate(a[1:]):
        while i >= 0 and a[i] < t:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = t
    return a
