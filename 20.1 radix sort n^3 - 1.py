from clrs import *
import random
import math

# 8.3-4 p200

def gen():
    n = random.randint(100,1000)
    k = n ** 3
    return [random.randint(0, k - 1) for _ in xrange(n)], k

def radix_sort(a, k):
    def counting_sort(a, i_shift):
        get_v = lambda n: (n >> i_shift * r) & mask
        b = list(a)
        c = [0] * kr
        a, b = b, a
        for n in a:
            v = get_v(n)
            c[v] += 1
        for i in xrange(1, kr):
            c[i] += c[i - 1]
        for i in xrange(len(a) - 1, -1, -1):
            n = a[i]
            v = get_v(n)
            c[v] -= 1
            b[c[v]] = n
    n = len(a)
    r = int(math.log(n, 2))
    kr = 2 ** r
    mask = 1
    for _ in xrange(r - 1):
        mask = (mask << 1) | 1
    lgk = int(math.ceil(math.log(k, 2)))
    m = (lgk + r - 1) // r
    for i_shift in xrange(m):
        counting_sort(a, i_shift)
    return a

@check
def _():
    a, k = gen()
    oa = list(a)
    ans = radix_sort(a, k)
    rans = sorted(oa)
    yield ans == rans
