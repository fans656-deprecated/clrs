import random

tester = None

def test(f):
    global tester
    tester = f

def check(arg):
    n = 100
    def check_deco(checker):
        def checker_(f):
            for _ in xrange(n):
                for ok in checker(f):
                    if ok:
                        break
                else:
                    raise Exception
                    break
        test(checker_)
    if callable(arg):
        f = arg
        return check_deco(f)
    else:
        n = arg
        return check_deco

def sort(f):
    a, ans = case.sa()
    yield f(a), ans

def answer(f):
    r = tester(f)
    if r:
        print r
    return f

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
