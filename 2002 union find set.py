# coding: utf-8
from clrs import *
import random

'''
http://blog.csdn.net/dm_vincent/article/details/7655764
http://blog.csdn.net/dm_vincent/article/details/7769159
'''
'''
http://acm.hdu.edu.cn/showproblem.php?pid=1213
'''

class UF(object):

    def __init__(self, n):
        self.parent = list(range(n))
        self.sizes = [1] * n
        self.n = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def find2(self, x):
        r = x
        while self.parent[r] != r:
            r = self.parent[r]
        while x != r:
            p = self.parent[x]
            self.parent[x] = r
            x = p
        return r

    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i != j:
            if self.sizes[i] < self.sizes[j]:
                i, j = j, i
            self.sizes[i] += self.sizes[j]
            self.parent[j] = i
            self.n -= 1
            return True
        return False

    def __len__(self):
        return self.n

    def __repr__(self):
        n = len(self.parent)
        sets = [[] for _ in xrange(n)]
        for i in xrange(n):
            self.find(i)
            sets[self.parent[i]].append(i)
        return ' '.join(str(t) for t in sets if t)

def test(uf, xys):
    for x, y in xys:
        uf.union(x, y)

#from f6 import *
#n = 1000000
#xys = [(random.randint(0, n - 1), random.randint(0, n - 1))
#       for _ in xrange(n)]
#with timeit():
#    test(UF(n), iter(xys))
#with timeit():
#    uf = UF(n)
#    uf.find = uf.find2
#    test(uf, iter(xys))
