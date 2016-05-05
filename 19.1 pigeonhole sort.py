# coding: utf-8
from clrs import *
import random

u'''
https://en.wikipedia.org/wiki/Pigeonhole_sort
pigeonhole 很适合用在链表上，跟 counting sort 的原理是一样的
只不过 c 数组里不放位置信息而放实际的元素
'''

@check
def _(f):
    a, rans = case.sa(simple=True)
    ans = from_linked_list(f(to_linked_list(a)))
    yield ans == rans
    print ans, rans

@answer
def pigeonhole_sort(node):
    p = node
    mi = ma = p.v
    while p.next:
        p = p.next
        if p.v < mi:
            mi = p.v
        elif p.v > ma:
            ma = p.v
    k = ma - mi + 1
    def hole():
        r = Node()
        return [r, r]
    c = [hole() for _ in xrange(k)]
    p = node
    while p:
        t = c[p.v - mi]
        t[1].next = Node(p.v)
        t[1] = t[1].next
        p = p.next
    r = e = Node()
    for first, last in c:
        if first.next:
            e.next = first.next
            e = last
    return r.next
