import collections
from typing import Optional, List

from trees.TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q: List[TreeNode] = [root]
        if not root:
            return []
        while q:
            nc = len(q)
            for i in range(len(q)):
                node = q.pop(0)
                if i == nc - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
