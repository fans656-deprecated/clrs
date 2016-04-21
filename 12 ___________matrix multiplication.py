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
