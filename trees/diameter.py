# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or
# may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional

from trees.TreeNode import TreeNode, maxDepth


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = maxDepth(root.left)
        rh = maxDepth(root.right)

        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)

        return max(lh+rh+1, max(ld, rd))
