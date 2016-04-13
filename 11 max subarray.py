from clrs import *
import random

def std(a):
    n = len(a)
    beg = end = 0
    ma = a[0]
    for i in xrange(n):
        cur = a[i]
        for j in xrange(i, n):
            if j != i:
                cur += a[j]
            if cur > ma:
                ma = cur
                beg = i
                end = j
    return sum(a[beg:end + 1])

@test
def _(f):
    for _ in xrange(100):
        a = [random.randint(-50,50) for _ in xrange(100)]
        oa = list(a)
        if f(a) != std(oa):
            raise Exception

@answer
def f(a):
    def max_sub(a, beg, end):
        def max_crossing_sub(a, beg, mid, end):
            cur = a[mid - 1]
            ma_left = cur
            for i in xrange(mid - 2, -1, -1):
                cur += a[i]
                if cur > ma_left:
                    ma_left = cur
            cur = a[mid]
            ma_right = cur
            for i in xrange(mid + 1, end):
                cur += a[i]
                if cur > ma_right:
                    ma_right = cur
            return ma_left + ma_right
        if end - beg <= 1:
            return a[beg]
        else:
            mid = (beg + end) // 2
            return max(max_sub(a, beg, mid),
                       max_sub(a, mid, end),
                       max_crossing_sub(a, beg, mid, end))
    return max_sub(a, 0, len(a))

@answer
def g(a):
    def max_sub(a, beg, end):
        def max_crossing_sub(a, beg, mid, end):
            cur = a[mid - 1]
            ma_left = cur
            for i in xrange(mid - 2, -1, -1):
                cur += a[i]
                if cur > ma_left:
                    ma_left = cur
            cur = a[mid]
            ma_right = cur
            for i in xrange(mid + 1, end):
                cur += a[i]
                if cur > ma_right:
                    ma_right = cur
            return ma_left + ma_right
        if end - beg < 60:
            return std(a[beg:end])
        else:
            mid = (beg + end) // 2
            return max(max_sub(a, beg, mid),
                       max_sub(a, mid, end),
                       max_crossing_sub(a, beg, mid, end))
    return max_sub(a, 0, len(a))

#a = [random.randint(-50,50) for _ in xrange(int(1000))]
#from f6 import timeit
#with timeit():
#    f(a)
#with timeit():
#    g(a)
