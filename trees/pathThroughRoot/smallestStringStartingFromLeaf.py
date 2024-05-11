# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters
# 'a' to 'z'. Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller. For example, "ab" is lexicographically
# smaller than "aba". A leaf of a node is a node that has no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq as hq


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        words = []

        def dfs(root, word, words):
            if not root:
                return

            word += chr(ord('a') + root.val)
            if not root.left and not root.right:
                words.append(word[::-1])
            dfs(root.left, word, words)
            dfs(root.right, word, words)
            word[:-1]

        dfs(root, "", words)
        words.sort()
        return words[0]
