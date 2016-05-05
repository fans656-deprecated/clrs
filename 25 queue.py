from clrs import *
import random

class Queue(object):

    def __init__(self, n=500):
        self.a = [0] * n
        self.max_n = n
        self.b, self.e = 0, 0

    def enqueue(self, x):
        if self.full():
            raise Exception('full')
        self.a[self.e] = x
        self.e = (self.e + 1) % self.max_n

    def dequeue(self):
        if not self:
            raise Exception('empty')
        r = self.a[self.b]
        self.b = (self.b + 1) % self.max_n
        return r

    def full(self):
        return self.e + 1 == self.b

    def __nonzero__(self):
        return self.b != self.e

class Queue2(object):

    def __init__(self, n=500):
        self.a = [0] * n
        self.max_n = n
        self.b, self.e = 0, 0
        self.added = False

    def enqueue(self, x):
        if self.full():
            raise Exception('full')
        self.a[self.e] = x
        self.e = (self.e + 1) % self.max_n

    def dequeue(self):
        if not self:
            raise Exception('empty')
        r = self.a[self.b]
        self.b = (self.b + 1) % self.max_n
        return r

    def full(self):
        return self.b == self.e and self.added

    def __nonzero__(self):
        return not (self.b == self.e and not self.added)

@check
def _():
    q = Queue()
    a = case.a()
    b = []
    i = 0
    n = len(a)
    while i < n:
        if not q or random.randint(0, 1):
            q.enqueue(a[i])
            i += 1
        else:
            b.append(q.dequeue())
    while q:
        b.append(q.dequeue())
    yield a == b

@check
def _():
    q = Queue2()
    a = case.a()
    b = []
    i = 0
    n = len(a)
    while i < n:
        if not q or random.randint(0, 1):
            q.enqueue(a[i])
            i += 1
        else:
            b.append(q.dequeue())
    while q:
        b.append(q.dequeue())
    yield a == b
