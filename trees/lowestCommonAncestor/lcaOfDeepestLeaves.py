# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deepestLeaves(root):
            if not root:
                return (0, [])

            def dfs(node, level):
                if not node:
                    return level, []

                if not node.left and not node.right:
                    return level, [node]

                left_level, left_leaves = dfs(node.left, level + 1)
                right_level, right_leaves = dfs(node.right, level + 1)

                if left_level > right_level:
                    return left_level, left_leaves
                elif left_level < right_level:
                    return right_level, right_leaves
                else:
                    return left_level, left_leaves + right_leaves

            deepest_level, deepest_leaves = dfs(root, 0)
            return deepest_leaves

        deepest_leaves = deepestLeaves(root)

        def lca(node, deepest_leaves):
            if not node or node in deepest_leaves:
                return node
            left = lca(node.left, deepest_leaves)
            right = lca(node.right, deepest_leaves)
            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        return lca(root, deepest_leaves)
