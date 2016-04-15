from clrs import *

@check
def _(f):
    a = [random.randint(0,100) for _ in xrange(100)]
    v = random.randint(0,100)
    i = f(v, a)
    try:
        ans = a.index(v)
    except ValueError:
        ans = None
    yield i == ans

@answer
def _(v, a):
    for i, t in enumerate(a):
        if t == v:
            return i
