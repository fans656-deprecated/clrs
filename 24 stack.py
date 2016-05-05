from clrs import *
import random

class Stack(object):

    def __init__(self, n=500):
        self.max_n = n
        self.a = [0] * n
        self.end = 0

    def push(self, x):
        if self.full():
            raise Exception('full')
        self.a[self.end] = x
        self.end += 1

    def pop(self):
        if not self:
            raise Exception('empty')
        self.end -= 1
        return self.a[self.end]

    def __nonzero__(self):
        return self.end != 0

    def full(self):
        return self.end == self.max_n

@check
def _():
    #random.seed(0)
    b = case.a()
    a = Stack()
    for t in b:
        a.push(t)
    i = 0
    while True:
        if random.randint(0, 2):
            if not a:
                assert not b
                break
            assert a.pop() == b.pop()
        else:
            a.push(i)
            b.append(i)
            i += 1
    yield True
