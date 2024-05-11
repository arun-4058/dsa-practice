# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right and is_left:
                return root.val
            left_sum = dfs(root.left, True)
            right_sum = dfs(root.right, False)
            return left_sum + right_sum

        return dfs(root, False)
