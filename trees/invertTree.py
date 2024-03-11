from typing import Optional

from trees.TreeNode import TreeNode, create_tree, level_traversal


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


node = create_tree()
level_traversal(node)
print("inverted tree :: ")
inverted = Solution().invertTree(node)
level_traversal(inverted)
