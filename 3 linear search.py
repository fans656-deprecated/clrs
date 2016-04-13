from clrs import *

@test
def _(f):
    for _ in xrange(100):
        a = [random.randint(0,100) for _ in xrange(100)]
        v = random.randint(0,100)
        i = f(v, a)
        try:
            ans = a.index(v)
        except ValueError:
            ans = None
        if not (i == ans):
            raise Exception(
                'Expect {}, got {}'.format(ans, i)
            )

@answer
def _(v, a):
    for i, t in enumerate(a):
        if t == v:
            return i
