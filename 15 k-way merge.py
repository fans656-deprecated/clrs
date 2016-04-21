from clrs import *
import random

left = lambda k: 2 * k + 1
right = lambda k: 2 * k + 2
parent = lambda k: (k - 1) // 2

class MinHeap(object):

    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        while i:
            p = parent(i)
            if x < self.a[p]:
                self.a[i] = self.a[p]
                i = p
            else:
                break
        self.a[i] = x

    def pop(self):
        r = self.a[0]
        self.a[0] = self.a[-1]
        del self.a[-1]
        self.heapify(0)
        return r

    def heapify(self, i):
        n = len(self.a)
        while True:
            l = left(i)
            r = right(i)
            oi = i
            if l < n and self.a[l] < self.a[i]:
                i = l
            if r < n and self.a[r] < self.a[i]:
                i = r
            if i != oi:
                self.a[i], self.a[oi] = self.a[oi], self.a[i]
            else:
                return

    def __nonzero__(self):
        return bool(self.a)

@check
def _(f):
    ars = [
        sorted([random.randint(-100,100)
                for j in xrange(random.randint(50,100))])
        for i in xrange(random.randint(2,10))
    ]
    a = f(*ars)
    rans = sorted(sum(ars, []))
    yield a == rans
    print a
    print rans

@answer
def f(*ars):

    class Key:

        def __init__(self, *vs):
            self.vs = vs

        def __lt__(self, o):
            return self.vs[0] < o.vs[0]

        def __iter__(self):
            return iter(self.vs)

    h = MinHeap()
    for a in ars:
        h.push(Key(a[0], a, 1))
    r = []
    while h:
        v, a, i = h.pop()
        r.append(v)
        if i < len(a):
            h.push(Key(a[i], a, i + 1))
    return r
