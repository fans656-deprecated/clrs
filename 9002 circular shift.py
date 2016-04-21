# coding: utf-8
from clrs import *
import random

u'''
把数组a循环移位k，方法：

(update 2016-04-21 16:33:17)
(
第一个方法是错的，比如
[0,1,2,3,4,5] >> 4
0 -> 4 -> 2 -> 0
循环了
于是还需要标记每个元素所在位置是否空出来，是否已放置了最终结果
空间复杂度会变成O(n)
)
1. 从第一个元素开始，移位k(模n)，挤掉本来在那的，新的元素没了地方呆，
去挤掉它要去的地方的元素，这么每次都把一个元素放到它最终的位置上，
执行n次，完成
O(n)

2. (A^-1 B^-1) ^ -1 == BA
先反转A和B，再反转整个数组
O(n)
'''

def reverse(a, b, e):
    e -= 1
    while b < e:
        a[b], a[e] = a[e], a[b]
        b += 1
        e -= 1

def std(a, k):
    n = len(a)
    if k < 0:
        k = -k
    else:
        k = n - k
    reverse(a, 0, k)
    reverse(a, k, n)
    reverse(a, 0, n)
    return a

def shift(a, k):
    n = len(a)
    i = 0
    u = a[i]
    for _ in xrange(len(a)):
        j = (i + n + k) % n
        v = a[j]
        a[j] = u
        u = v
        i = j
    return a

@check
@ignore
def _():
    a = case.a()
    a = range(6)
    oa = list(a)
    for k in xrange(100):
        ans, rans = shift(a, k), std(oa, k)
        if ans != rans:
            yield False
            print ans, rans
