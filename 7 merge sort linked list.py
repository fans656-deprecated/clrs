from clrs import *
import random

@test
def _(f):
    for _ in xrange(100):
        a = [random.randint(0,100) for _ in xrange(50)]
        rans = sorted(a)
        node = to_linked_list(a)
        ans = from_linked_list(f(node))
        if ans != rans:
            print ans
            print rans
            raise Exception

@answer
def f(node):
    def take_run(head, n):
        if not head:
            return None, None
        p = head
        n -= 1
        while n and p.next:
            p = p.next
            n -= 1
        new_head = p.next
        p.next = None
        return head, new_head
    def merge(tail, a, b):
        while a and b:
            if a.v <= b.v:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        p = a if a else b
        tail.next = p
        while tail.next:
            tail = tail.next
        return tail
    n = 0
    p = node
    while p:
        p = p.next
        n += 1
    head = tail = Node()
    run_len = 1
    while run_len < n:
        while True:
            a, node = take_run(node, run_len)
            b, node = take_run(node, run_len)
            tail = merge(tail, a, b)
            if not b:
                break
        node = head.next
        tail = head
        run_len *= 2
    return head.next
