# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, targetSum, currSum) -> bool:
            if not root:
                return False

            currSum += root.val

            if not root.right and not root.left:
                if currSum == targetSum:
                    return True
            else:
                return dfs(root.left, targetSum, currSum) or dfs(root.right, targetSum, currSum)
            currSum -= root.val

        return dfs(root, targetSum, 0)

