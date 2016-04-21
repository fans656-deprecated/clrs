# coding: utf-8
from clrs import *
import random

u'''
为了避免数组中元素全部相同导致(即使randomized)快排的最坏时间复杂度
把数组划分为3个部分：< pivot 的，= pivot 的，> pivot 的

这是一个荷兰国旗问题：把一个只有 0,1,2 三种元素的数组 permute 使得
最后是 0...0 1...1 2...2

通过在首尾设置区间的办法 O(n) 搞定，不禁想如果有4种类别的元素呢？
首2个区间，尾2个区间，也可以
5种呢？m种呢？
区间法都可以做到，但是 m 种最终导致复杂度成为 O(nm)

而一次遍历统计不同类别的出现次数，再一次遍历填充，还是 O(n)
统计的方式，如果 m 种类别规规矩矩地用 0,1,2..m-1 表示，数组就可以
否则得用hash表

假设预先不知道 m 的大小呢？没法设置区间了，那还是遍历吧，O(n)
但你发现没有，整个排下序也可以搞定 O(nlgn)

从 quick sort 的 partition 一路延伸到了 comparison sort 和 linear time sort
神奇
'''

def group(a, m):
    l = [len(a)] * (m + 1)
    for t in a:
        for i in xrange(t):
            b = l[i]
            e = l[i + 1]
            if e - b > 0:
                a[b - 1] = a[e - 1]
            l[i] -= 1
        l[t] -= 1
        a[l[t]] = t

@check
def _():
    m = random.randint(2,50)
    a = [random.randint(0,m-1) for _ in xrange(100)]
    group(a, m)
    yield all(a[i] <= a[i + 1] for i in xrange(len(a) - 1))
