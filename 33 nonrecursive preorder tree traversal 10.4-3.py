u'''
https://leetcode.com/problems/binary-tree-preorder-traversal/

10.4-3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        st = [root]
        result = []
        while st:
            node = st.pop()
            if node:
                result.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return result
