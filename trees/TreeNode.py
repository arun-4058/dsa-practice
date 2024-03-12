from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if (p and not q) or (not p and q):
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)


def level_traversal(root: Optional[TreeNode]) -> None:
    if not root:
        return None
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print(node.val)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def traverse(root: Optional[TreeNode]) -> None:
    if not root:
        return
    traverse(root.left)
    print(root.val)
    traverse(root.right)


def create_tree() -> TreeNode:
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root
