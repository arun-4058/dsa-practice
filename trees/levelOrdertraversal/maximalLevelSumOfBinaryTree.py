# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root, 1)]
        max_level = 1
        max_sum = float("-inf")

        while len(q) > 0:
            level_sum = 0
            level_size = len(q)
            for _ in range(level_size):
                node, level = q.pop(0)
                level_sum += node.val

                if node.left:   q.append((node.left, level + 1))
                if node.right:  q.append((node.right, level + 1))

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
        return max_level

        return res