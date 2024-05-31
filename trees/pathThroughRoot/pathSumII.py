# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        if not root:
            return paths

        def dfs(root, targetSum, currSum, path, paths):
            if not root:
                return

            currSum += root.val
            path.append(root.val)
            if root.right == None and root.left == None:
                if currSum == targetSum:
                    paths.append(list(path))
            else:
                dfs(root.left, targetSum, currSum, path, paths)
                dfs(root.right, targetSum, currSum, path, paths)

            path.pop()
            currSum -= targetSum

        dfs(root, targetSum, 0, [], paths)
        return paths

