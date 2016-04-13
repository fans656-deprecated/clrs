import random

tester = None

def test(f):
    global tester
    tester = f

def answer(f):
    r = tester(f) or 'Accept!'
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
