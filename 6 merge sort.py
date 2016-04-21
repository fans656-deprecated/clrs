from clrs import *
import random

@check
def _(f):
    a = [1,2,3,4,5]
    oa = list(a)
    random.shuffle(a)
    a = f(a)
    yield a == [1,2,3,4,5]

def merge(a, beg, mid, end):
    left = a[beg:mid] + [float('inf')]
    right = a[mid:end] + [float('inf')]
    i, j = 0, 0
    for k in xrange(beg, end):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

@answer
def _(a):
    def sort(a, beg, end):
        if beg + 1 >= end:
            return
        mid = (end + beg) // 2
        sort(a, beg, mid)
        sort(a, mid, end)
        merge(a, beg, mid, end)
        return a
    return sort(a, 0, len(a))

# bottom up version
@answer
def _(a):
    n = len(a)
    run_len = 1
    while run_len < n:
        for i in xrange(0, len(a), 2 * run_len):
            merge(a, i, min(i + run_len, n), min(i + 2 * run_len, n))
        run_len *= 2
    return a

# ==================== practice

@answer
def _(a):
    def merge_sort(a, beg, end):
        def merge(a, beg, mid, end):
            i = beg
            j = mid
            b = []
            while i < mid and j < end:
                if a[i] <= a[j]:
                    b.append(a[i])
                    i += 1
                else:
                    b.append(a[j])
                    j += 1
            b += a[i:mid]
            b += a[j:end]
            a[beg:end] = b
        if end - beg > 1:
            mid = (beg + end) // 2
            merge_sort(a, beg, mid)
            merge_sort(a, mid, end)
            merge(a, beg, mid, end)
    merge_sort(a, 0, len(a))
    return a

@answer
def _(a):
    def merge(a, beg, mid, end):
        i = beg
        j = mid
        b = []
        while i < mid and j < end:
            if a[i] <= a[j]:
                b.append(a[i])
                i += 1
            else:
                b.append(a[j])
                j += 1
        b += a[i:mid]
        b += a[j:end]
        a[beg:end] = b
    n = len(a)
    run_len = 1
    while run_len < n:
        for i in xrange(0, n, 2 * run_len):
            merge(a, i, min(n, i + run_len), min(n, i + 2 * run_len))
        run_len *= 2
    return a
