from typing import Optional, List

from trees.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # this is not an efficient solution
        def inorder(node: TreeNode, res: List[int]) -> List[int]:
            if not node:
                return []
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
            return res

        return inorder(root, [])[k - 1]
