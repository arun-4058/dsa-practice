from typing import Optional, List

from trees.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        while len(q) > 0:
            nc = len(q)
            ln = []
            while nc > 0:
                node = q.pop(0)
                ln.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                nc = nc-1
            res.append(ln)
        return res

