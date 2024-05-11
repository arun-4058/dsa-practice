# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        def mergeSortedList(list1, list2):
            m, n = len(list1), len(list2)
            res = []
            i, j = 0, 0
            while i < m and j < n:
                if list1[i] <= list2[j]:
                    res.append(list1[i])
                    i += 1
                else:
                    res.append(list2[j])
                    j += 1

            while i < m:
                res.append(list1[i])
                i += 1
            while j < n:
                res.append(list2[j])
                j += 1
            return res

        node1, node2 = [], []
        dfs(root1, node1)
        dfs(root2, node2)

        return mergeSortedList(node1, node2)
