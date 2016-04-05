from clrs import *

class Node(object):

    def __init__(self, v):
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

@test
def _(f):
    for _ in xrange(100):
        a = [1,2,3,4,5]
        oa = list(a)
        random.shuffle(a)
        a = from_linked_list(f(to_linked_list(a)))
        if a != [1,2,3,4,5]:
            raise Exception(
                'Expect {}, got {}'.format(oa, a)
            )

@answer
# selection sort
def _(head):
    ret = head
    while head:
        cur = head
        mi = cur
        while cur:
            if cur.v < mi.v:
                mi = cur
            cur = cur.next
        t = head.v
        head.v = mi.v
        mi.v = t
        head = head.next
    return ret
