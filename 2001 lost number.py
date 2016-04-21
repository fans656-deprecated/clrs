# coding: utf-8
from clrs import *
import random

'''
http://blog.csdn.net/morewindows/article/details/12684497
'''

u'''
数组a中的数，除了一个只出现过一次外，其他都出现过两次
找到这个只出现过一次的元素
'''
@check
def _(f):
    a = list(set(random.randint(-100,100) for _ in xrange(100)))
    rans = a[0]
    a += a[1:]
    random.shuffle(a)
    oa = list(a)
    yield f(a) == rans

@answer
def f(a):
    x = a[0]
    for t in a[1:]:
        x ^= t
    return x

# O(nlgn), O(lg) if sorted
@answer
def f(a):
    if len(a) == 1:
        return a[0]
    a.sort()
    beg, end = 0, len(a)
    while True:
        #print a
        if beg >= end:
            print a
            exit()
        if a[beg] != a[beg+1]:
            return a[beg]
        elif a[end-1] != a[end-2]:
            return a[end-1]
        mid = beg + (end - beg) // 2
        odd = (mid - beg) & 1
        #print beg, end, mid, a[mid]
        #raw_input()
        if a[mid] == a[mid - 1]:
            if odd:
                beg = mid + 1
            else:
                end = mid - 1
        elif a[mid] == a[mid + 1]:
            if odd:
                end = mid
            else:
                beg = mid + 2
        else:
            return a[mid]
#print f([-9, -9, -6, -6, -5, -5, -2, -2, 2, 4, 4])
#exit()

u'''
本来每个数都该出现2次，结果有2个只出现了1次，找出这俩数
'''
@check
def _(f):
    for _ in xrange(100):
        a = list(set(random.randint(-100,100) for _ in xrange(100)))
        rans = a[0], a[1]
        rans2 = a[1], a[0]
        a += a[2:]
        random.shuffle(a)
        oa = list(a)
        ans = f(a)
        yield ans == rans or ans == rans2

@answer
def f(a):
    diff = a[0]
    for t in a[1:]:
        diff ^= t
    splitter = 1
    while not splitter & diff:
        splitter <<= 1
    x = y = 0
    for t in a:
        if t & splitter:
            x ^= t
        else:
            y ^= t
    return x, y

u'''
本来每个数都该出现3次，结果有1个只出现了1次，找出这数
'''
@check
def _(f):
    for _ in xrange(100):
        a = list(set(random.randint(-9,9) for _ in xrange(2)))
        rans = a[0]
        a += a[1:] * 2
        random.shuffle(a)
        oa = list(a)
        ans = f(a)
        if ans ^ rans != 0:
            print ans, rans, a
            print bin(ans), bin(rans)
            raise Exception

##@answer
#def f(a):
#    count = [0] * 32
#    for t in a:
#        for i in xrange(32):
#            if t & (1 << i):
#                count[i] += 1
#    r = 0
#    for i in xrange(32):
#        if count[i] % 3:
#            r |= 1 << i
#    return r
#
#print f([-1,-2,-2,-2])

u'''
本应出现u次，但现在有m个异常的数，出现的次数不是u次

这个问题排序后遍历就好了——O(nlgn)
上面的那些是有O(n)解法的特例
'''
