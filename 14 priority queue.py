from clrs import *
import operator
import random

left = lambda k: 2 * k + 1
right = lambda k: 2 * k + 2
parent = lambda k: (k - 1) // 2

class Heap(object):

    def __init__(self, op=operator.gt):
        self.a = []
        self.op = op

    def pop(self):
        r = self.a[0]
        self.a[0] = self.a[-1]
        del self.a[-1]
        self.heapify(0)
        return r

    def top(self):
        return self.a[0]

    def insert(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        while i:
            p = parent(i)
            if self.op(x, self.a[p]):
                self.a[i] = self.a[p]
                i = p
            else:
                break
        self.a[i] = x

    def change(self, i, x):
        if i < len(self.a):
            if self.op(self.a[i], x):
                self.a[i] = x
                self.heapify(i)
            elif self.op(x, self.a[i]):
                while i:
                    p = parent(i)
                    if self.op(x, self.a[p]):
                        self.a[i] = self.a[p]
                        i = p
                    else:
                        break
                self.a[i] = x

    def heapify(self, i):
        n = len(self.a)
        while True:
            l = left(i)
            r = right(i)
            oi = i
            if l < n and self.op(self.a[l], self.a[i]):
                i = l
            if r < n and self.op(self.a[r], self.a[i]):
                i = r
            if i != oi:
                self.a[i], self.a[oi] = self.a[oi], self.a[i]
            else:
                return

def is_heap(h):
    a = h.a
    op = h.op
    n = len(a)
    for i in xrange(len(a)):
        l = left(i)
        r = right(i)
        if l < n and op(a[l], a[i]):
            return False
        if r < n and op(a[r], a[i]):
            return False
    return True

@check
def _(f):
    h = Heap()
    a = case.a()
    for x in a:
        h.insert(x)
    yield is_heap(h)

@check
def _(f):
    h = Heap()
    a = case.a()
    for x in a:
        h.insert(x)
        if random.randint(0,2) == 0:
            i = random.randint(0, len(h.a) - 1)
            dx = random.randint(-100, 100)
            h.change(i, h.a[i] + dx)
            assert is_heap(h)
    yield is_heap(h)

@check
def _(_):
    q = Heap(op=operator.lt)
    a = case.a()
    b = []
    i = 0
    count = 0
    while len(b) < len(a):
        if not q.a or (i < len(a) and random.randint(0,1) == 0):
            q.insert((count, a[i]))
            count += 1
            i += 1
        else:
            t = q.pop()[1]
            b.append(t)
    yield a == b

#@check
def _(_):
    q = Heap()
    a = case.a()
    b = []
    count = 0
    while len(q.a) < len(a):
        q.insert((count, a[count]))
        count += 1
    while len(q.a):
        t = q.pop()[1]
        b.append(t)
