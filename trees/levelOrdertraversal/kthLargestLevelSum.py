# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        res = []
        while len(q) > 0:
            nc = len(q)
            level_sum = 0
            for _ in range(nc):
                node = q.pop(0)
                level_sum += node.val

                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            res.append(level_sum)
        res.sort(reverse=True)
        # heapq.heappush(heap, level_sum)
        # if len(heap) > k:
        #     heapq.heappop(heap)
        return -1 if k > len(res) else res[k - 1]
