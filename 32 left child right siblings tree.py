class Node(object):

    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_sibling = None

    def __repr__(self):
        return str(self.val)

def build(a):
    if not isinstance(a, list):
        return Node(a)
    if not a:
        return None
    nodes = map(build, a)
    root = nodes[0]
    if len(nodes) > 1:
        root.left_child = nodes[1]
    for i in xrange(1, len(nodes) - 1):
        nodes[i].right_sibling = nodes[i + 1]
    return root

def show(root, depth=0):
    if not root:
        return
    print '  ' * depth + str(root.val)
    c = root.left_child
    while c:
        show(c, depth + 1)
        c = c.right_sibling

def preorder(root, result=[]):
    if root:
        result.append(root)
        c = root.left_child
        while c:
            preorder(c, result)
            c = c.right_sibling
    return result

def postorder(root, result=[]):
    if root:
        c = root.left_child
        while c:
            postorder(c, result)
            c = c.right_sibling
        result.append(root)
    return result

root = build(
    [1, 2, [3, 5], [4, 6, 7]]
)
show(root)
print preorder(root)
print postorder(root)
