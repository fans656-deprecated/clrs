from clrs import *
import random

class Stack(object):

    def __init__(self, n=500):
        self.a = [0] * n
        self.max_n = n
        self.left_end = 0
        self.right_beg = n

    def left_empty(self):
        return self.left_end == 0

    def right_empty(self):
        return self.right_beg == self.max_n

    def __nonzero__(self):
        return not self.left_empty() or not self.right_empty()

    def full(self):
        return not (self.left_end < self.right_beg)

    def push(self, x):
        if self.full():
            raise Exception('full')
        self.a[self.left_end] = x
        self.left_end += 1

    def push2(self, x):
        if self.full():
            raise Exception('full')
        self.right_beg -= 1
        self.a[self.right_beg] = x

    def pop(self):
        if self.left_empty():
            raise Exception('empty')
        self.left_end -= 1
        return self.a[self.left_end]

    def pop2(self):
        if self.right_empty():
            raise Exception('empty')
        r = self.a[self.right_beg]
        self.right_beg += 1
        return r

    def __repr__(self):
        return ''.join(
            map(str, (self.a[:self.left_end], self.a[self.right_beg:])))

def deco():
    def deco_(f):
        def f_(self, *args, **kwargs):
            f(self, *args, **kwargs)
            print self
        return f_
    Stack.push = deco_(Stack.push)
    Stack.push2 = deco_(Stack.push2)
    Stack.pop = deco_(Stack.pop)
    Stack.pop2 = deco_(Stack.pop2)
deco()

st = Stack()
st.push(1)
st.pop()
st.push2(1)
st.push2(2)
st.push2(3)
st.pop2()
st.pop2()
st.pop2()
