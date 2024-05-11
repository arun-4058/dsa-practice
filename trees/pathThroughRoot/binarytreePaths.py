# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path, paths = [], []
        if not root:
            return paths

        def dfs(root, path, paths):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append('->'.join(path))

            dfs(root.left, path, paths)
            dfs(root.right, path, paths)

            path.pop()

        dfs(root, path, paths)
        return paths