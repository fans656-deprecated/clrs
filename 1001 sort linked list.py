from clrs import *

@check
def _(f):
    a = [1,2,3,4,5]
    oa = list(a)
    random.shuffle(a)
    a = from_linked_list(f(to_linked_list(a)))
    yield a == [1,2,3,4,5]

# selection sort
@answer
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
