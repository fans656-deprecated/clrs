from clrs import *
import math
import random

def std(a, b):
    n = int(math.sqrt(len(a)))
    c = [0] * (n * n)
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                c[n * i + j] += a[n * i + k] * b[n * k + j]
    return c

@test
def _(f):
    for _ in xrange(100):
        n = random.randint(2,10)
        a = [random.randint(-50,50) for _ in xrange(n * n)]
        b = [random.randint(-50,50) for _ in xrange(n * n)]
        if f(a, b) != std(a, b):
            raise Exception

@answer
def f(a, b):
    def mul(c, a, am, b, bm):
        def split(metric):
            r, c, n, m = metric
            np = n // 2
            r_mid = i + np
            mp = m // 2
            c_mid = j + mp
            return (
                (r, c, np, mp),
                (r, c + mp, np, m - mp),
                (r + np, c, n - np, m),
                (r + np, c + mp, n - np, m - mp),
            )
        if am[2] == am[3] == bm[2] == bm[3] == 1:
            c[n * cm[0] + cm[1]] = a[n * am[0] + am[1]] * b[n * bm[0] + bm[1]]
        else:
            a11, a12, a21, a22 = split(am)
            b11, b12, b21, b22 = split(bm)
            mul(c, a, a11, b, )
