from typing import Optional

from trees.TreeNode import TreeNode, maxDepth


class Solution:

    # this is a recursive method of checking if the tree is height balanced or not
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lh = maxDepth(root.left)
        rh = maxDepth(root.right)
        if abs(lh - rh) > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)

    def is_balanced_dfs(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]