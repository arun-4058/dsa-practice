# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getLevelSum(self, root) -> int:
        level_sum = 0
        if root.val % 2 == 0:
            q = [(root, 1)]
            while len(q) > 0:
                nc = len(q)
                for _ in range(nc):
                    node, level = q.pop(0)
                    if node.left:   q.append((node.left, level + 1))
                    if node.right:  q.append((node.right, level + 1))

                    if level == 3:
                        level_sum += node.val
        return level_sum

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # using dfs
        def dfs(node, parent, grandparent) -> int:
            nonlocal total_sum
            if not node:
                return

            if grandparent and grandparent.val % 2 == 0:
                total_sum += node.val

            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        total_sum = 0
        dfs(root, None, None)
        return total_sum

        # even_gp_sum = 0
        # if not root:
        #     return even_gp_sum

        # q = [root]
        # while len(q) > 0:
        #     nc = len(q)

        #     for _ in range(nc):
        #         node = q.pop(0)
        #         even_gp_sum += self.getLevelSum(node)

        #         if node.left:   q.append(node.left)
        #         if node.right:  q.append(node.right)
        # return even_gp_sum