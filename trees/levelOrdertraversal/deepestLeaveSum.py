# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # Perform a level-order traversal to find the deepest level
        queue = [root]
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # After processing all nodes at the current level, check if there are more levels
            if not queue:
                return level_sum



