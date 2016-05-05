# coding: utf-8

u'''
二叉树的先序、后序、中序遍历的三种实现方式

1. 递归方式(trival)
2. 循环方式(使用stack)
3. O(1)空间复杂度的循环方式

先序循环用栈比较简单，初始栈中放根元素
之后每取出一个元素就输出到结果，然后右孩子、左孩子依次入栈
再取再输出再入，直到栈空
注意是右孩子先于左孩子入栈，因为出栈顺序是反的

后序其实跟先序的结果是反的：父节点在左右子树之后
所以把先序的结果逆序就好了——但注意改成左孩子、右孩子依次入栈

中序需要添加信息，表明这个节点的左右子树处理过了没有



空间复杂度O(1)的算法是这里看的：
http://tech.technoflirt.com/2011/03/04/non-recursive-tree-traversal-in-on-using-constant-space/

实现时发现travel实际上是个独立的过程，先后中序只需要在每个节点判断路线形态就好了

评论里有travel的其他实现
travel2 代码更少

评论里甚至有只用一个指针的noneRecursiveTraversWithParentPointer
没仔细看
'''

from clrs import *
import random

class Node(object):

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

left = lambda k: k * 2 + 1
right = lambda k: k * 2 + 2
parent = lambda k: (k - 1) // 2

def tree_seed(n=100):
    nodes = [Node(t) for t in xrange(n)]
    exists = [random.randint(0,1) == 0 for _ in xrange(n)]
    return nodes, exists

def grow((nodes, exists)):
    n = len(nodes)
    nodes = [node if exist else None for node, exist in zip(nodes, exists)]
    for i in xrange(n):
        node = nodes[i]
        if node:
            l = left(i)
            if l < n:
                node.left = nodes[l]
                if node.left:
                    node.left.parent = node
            r = right(i)
            if r < n:
                node.right = nodes[r]
                if node.right:
                    node.right.parent = node
    return nodes[0]

def show(root, depth=0, visible=False):
    indent = '  ' * depth
    if root is None:
        if visible:
            print indent + str(None)
        return
    print indent + str(root.val)
    child_visible = root.left or root.right
    show(root.left, depth + 1, child_visible)
    show(root.right, depth + 1, child_visible)

def preorder_recursive(root, result):
    if root:
        result.append(root)
        preorder_recursive(root.left, result)
        preorder_recursive(root.right, result)
    return result

def postorder_recursive(root, result):
    if root:
        postorder_recursive(root.left, result)
        postorder_recursive(root.right, result)
        result.append(root)
    return result

def inorder_recursive(root, result):
    if root:
        inorder_recursive(root.left, result)
        result.append(root)
        inorder_recursive(root.right, result)
    return result

def preorder_iterative(root):
    result = []
    st = [root]
    while st:
        node = st.pop()
        if node:
            result.append(node)
            st.append(node.right)
            st.append(node.left)
    return result

def postorder_iterative(root):
    result = []
    st = [root]
    while st:
        node = st.pop()
        if node:
            result.append(node)
            st.append(node.left)
            st.append(node.right)
    return list(reversed(result))

def inorder_iterative(root):
    result = []
    st = [(root, False)]
    while st:
        node, done = st.pop()
        if node:
            if done:
                result.append(node)
            else:
                st.append((node.right, False))
                st.append((node, True))
                st.append((node.left, False))
    return result

u'''
https://github.com/leetcoders/LeetCode/blob/master/BinaryTreeInorderTraversal.h
这里的方法不需要存额外信息
'''
def inorder_iterative(root):
    result = []
    st = []
    cur = root
    while cur or st:
        while cur:
            st.append(cur)
            cur = cur.left
        node = st.pop()
        result.append(node)
        cur = node.right
    return result

def o1space_travel(root, f):
    cur = root
    prev = None
    while cur:
        f(cur, prev)
        if cur.parent == prev:
            prev = cur
            if cur.left:
                cur = cur.left
            elif cur.right:
                cur = cur.right
            else:
                cur = cur.parent
        elif cur.left == prev:
            prev = cur
            if cur.right:
                cur = cur.right
            else:
                cur = cur.parent
        elif cur.right == prev:
            prev = cur
            cur = cur.parent

def o1space_travel2(root, f):
    cur = root
    prev = None
    while cur:
        f(cur, prev)
        new_prev = cur
        if cur.left and cur.parent == prev:
            cur = cur.left
        elif cur.right and cur.right != prev:
            cur = cur.right
        else:
            cur = cur.parent
        prev = new_prev
#o1space_travel = o1space_travel2

def preorder_o1space(root):
    result = []
    def f(cur, prev):
        if cur.parent == prev:
            result.append(cur)
    o1space_travel(root, f)
    return result

def postorder_o1space(root):
    result = []
    def f(cur, prev):
        if cur.right and cur.right == prev:
            pass
        elif cur.left and not cur.right and cur.left == prev:
            pass
        elif not (cur.left or cur.right) and cur.parent == prev:
            pass
        else:
            return
        result.append(cur)
    o1space_travel(root, f)
    return result

def inorder_o1space(root):
    result = []
    def f(cur, prev):
        if cur.left and cur.left == prev:
            pass
        elif not cur.left and cur.right and cur.parent == prev:
            pass
        elif not (cur.left or cur.right):
            pass
        else:
            return
        result.append(cur)
    o1space_travel(root, f)
    return result

def tree(n=100):
    seed = tree_seed(n)
    root = grow(seed)
    return root

def build(a):
    if a is None or a == []:
        return None
    if not isinstance(a, list):
        return Node(a)
    nodes = map(build, a)
    root = nodes[0]
    if len(a) > 1:
        root.left = nodes[1]
        if root.left:
            root.left.parent = root
    if len(a) > 2:
        root.right = nodes[2]
        if root.right:
            root.right.parent = root
    return root

random.seed(4)

@check
def _():
    root = tree(5)
    #root = build(
    #    [1, [2, [3, None, 4], 5], [6, 7, [8, 9]]],
    #)
    #show(root)
    #print inorder_iterative(root)
    #exit()

    preorder = preorder_recursive(root, [])
    postorder = postorder_recursive(root, [])
    inorder = inorder_recursive(root, [])

    assert preorder_iterative(root) == preorder
    assert postorder_iterative(root) == postorder
    assert inorder_iterative(root) == inorder

    assert preorder_o1space(root) == preorder
    assert postorder_o1space(root) == postorder
    assert inorder_o1space(root) == inorder

    yield True
