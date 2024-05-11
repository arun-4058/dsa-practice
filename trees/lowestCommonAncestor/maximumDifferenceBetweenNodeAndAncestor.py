# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val, min_val):
            if not node:
                return 0
            max_val = max(node.val, max_val)
            min_val = min(node.val, min_val)

            diff1 = abs(node.val - max_val)
            diff2 = abs(node.val - min_val)

            left_diff = dfs(node.left, max_val, min_val)
            right_diff = dfs(node.right, max_val, min_val)

            return max(diff1, diff2, left_diff, right_diff)

        return dfs(root, root.val, root.val)




