from clrs import *

@check
def _(f):
    a, rans = case.sa()
    rans = list(reversed(rans))
    yield f(a) == rans

@answer
def _(a):
    for i, t in enumerate(a[1:]):
        while i >= 0 and a[i] < t:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = t
    return a
