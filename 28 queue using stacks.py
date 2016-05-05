u'''
https://leetcode.com/problems/implement-queue-using-stacks/
'''

class Queue(object):
    def __init__(self):
        self.popper = []
        self.pusher = []

    def push(self, x):
        self.pusher.append(x)

    def pop(self):
        if self.empty():
            raise Exception('empty')
        self.populate_popper()
        return self.popper.pop()

    def peek(self):
        if self.empty():
            raise Exception('empty')
        self.populate_popper()
        return self.popper[-1]

    def empty(self):
        return not self.popper and not self.pusher

    def populate_popper(self):
        if not self.popper:
            while self.pusher:
                self.popper.append(self.pusher.pop())
