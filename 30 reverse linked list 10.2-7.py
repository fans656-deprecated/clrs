u'''
10.2-7
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        p = head
        q = p.next if p else None
        r = q.next if q else None
        while q:
            q.next = p
            p = q
            q = r
            r = r.next if r else None
        if head:
            head.next = None
        head = p
        return head
