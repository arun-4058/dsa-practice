from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


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
