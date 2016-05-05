# coding: utf-8
u'''
https://leetcode.com/problems/implement-stack-using-queues/

有两种做法：
1. 两个队列分别作为 push 操作 和 pop 操作的角色
   此时 populate_popper 转移元素后需要把只有一个元素的那个队列变成popper
   而 push 操作需要检查 popper 是否有元素，如果有，放入 pusher
2. 两个队列叠在一起变成栈，类比两个叠着放的缸
   push 永远在后一个队列上进行
   populate 的含义是把栈中元素进一步压到下面的缸里，但是上面的缸留一个元素
   所以pop操作取掉了上面缸中的元素，需要交换上下缸的位置
'''

from collections import deque

class Stack(object):
    def __init__(self):
        self.pusher = deque()
        self.popper = deque()

    def push(self, x):
        if self.popper:
            self.pusher.append(self.popper.popleft())
        self.pusher.append(x)

    def pop(self):
        self.populate_popper()
        return self.popper.popleft()

    def top(self):
        self.populate_popper()
        return self.popper[0]

    def empty(self):
        return not self.pusher and not self.popper

    def populate_popper(self):
        if self.empty():
            raise Exception('empty')
        if not self.popper:
            while True:
                r = self.pusher.popleft()
                if not self.pusher:
                    self.pusher.append(r)
                    break
                self.popper.append(r)
            self.pusher, self.popper = self.popper, self.pusher

class Stack(object):

    def __init__(self):
        self.upper = deque()
        self.lower = deque()

    def push(self, x):
        self.upper.append(x)

    def pop(self):
        self.leave_one_in_upper()
        r = self.upper.popleft()
        self.upper, self.lower = self.lower, self.upper
        return r

    def top(self):
        self.leave_one_in_upper()
        return self.upper[0]

    def empty(self):
        return not self.upper and not self.lower

    def leave_one_in_upper(self):
        if self.empty():
            raise Exception('empty')
        while True:
            r = self.upper.popleft()
            if not self.upper:
                self.upper.append(r)
                break
            self.lower.append(r)

# class Stack(object):
#
#     def __init__(self):
#
#     def push(self, x):
#
#     def pop(self):
#
#     def top(self):
#
#     def empty(self):
#
