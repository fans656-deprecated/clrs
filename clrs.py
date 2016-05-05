import random
import inspect

class CLRS(object):

    def __init__(self):
        self.case = None
        self.n_cases = 100

    def check(self, case):
        self.case = case
        if not len(inspect.getargspec(case).args):
            self.run()

    def ignore(self, _):
        def f(self):
            yield True
        return f

    def answer(self, f):
        self.run(f)
        return f

    def run(self, *args, **kwargs):
        for i in xrange(self.n_cases):
            oks = self.case(*args, **kwargs)
            for ok in oks:
                if ok:
                    break
                else:
                    try:
                        next(oks)
                    except StopIteration:
                        pass
                    raise Exception

clrs = CLRS()

check = clrs.check
answer = clrs.answer
ignore = clrs.ignore

def sort(f):
    a, ans = case.sa()
    yield f(a), ans

class Node(object):

    def __init__(self, v=None):
        self.v = v
        self.next = None

def to_linked_list(a):
    nodes = [Node(t) for t in a]
    for a, b in zip(nodes[:-1], nodes[1:]):
        a.next = b
    return nodes[0]

def from_linked_list(node):
    a = []
    while node:
        a.append(node.v)
        node = node.next
    return a

class Case(object):

    def a(self, bound=(-100,100), n=100, simple=False):
        '''
        random array
        '''
        if simple:
            lo, hi = 0, 9
            n = 5
        else:
            if isinstance(bound, tuple):
                lo, hi = bound
            else:
                lo, hi = 0, bound
        return [random.randint(lo, hi) for _ in xrange(n)]

    def sa(self, *args, **kwargs):
        '''
        a and sorted(a)
        '''
        a = self.a(*args, **kwargs)
        return a, sorted(a)

case = Case()

if __name__ == '__main__':
    import os
    import imp

    excludes = [__file__]

    for fname in os.listdir('.'):
        if fname.endswith('.py') and fname not in excludes:
            print fname,
            imp.load_source('', fname)
            print 'tested'
            os.remove(fname[:-2] + 'pyc')
