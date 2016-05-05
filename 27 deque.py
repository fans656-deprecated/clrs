from clrs import *
import random

class Deque(object):

    def __init__(self, n=500):
        self.a = [0] * n
        self.max_n = n
        self.b = 0
        self.e = 0

    def push(self, x):
        if self.full():
            raise Exception('full')
        self.a[self.e] = x
        self.e = (self.e + 1) % self.max_n

    def pop(self):
        if not self:
            raise Exception('empty')
        self.e = (self.e + self.max_n - 1) % self.max_n
        return self.a[self.e]

    def pushleft(self, x):
        if self.full():
            raise Exception('full')
        self.b = (self.b + self.max_n - 1) % self.max_n
        self.a[self.b] = x

    def popleft(self):
        if not self:
            raise Exception('empty')
        r = self.a[self.b]
        self.b = (self.b + 1) % self.max_n
        return r

    def full(self):
        return self.e + 1 == self.b

    def __nonzero__(self):
        return self.b != self.e

q = Deque(5)
# pop right
try:
    q.pop()
except Exception as e:
    assert str(e) == 'empty'
# pop left
try:
    q.popleft()
except Exception as e:
    assert str(e) == 'empty'
