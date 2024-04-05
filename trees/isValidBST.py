from typing import Optional, List

from trees.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: TreeNode, left: int, right: int) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, int("-inf"), int("inf"))