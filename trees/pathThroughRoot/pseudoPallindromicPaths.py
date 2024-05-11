# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be
# pseudo-palindromic if at least one permutation of the node values in the path is a palindrome. 
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def dfs(node, freq):
            if not node:
                return 0

            # Update the frequency of the current node's value
            freq[node.val] += 1

            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                print(freq)
                odd_freq_count = sum(1 for count in freq if count % 2 != 0 and count != 0)
                # If at most one digit has an odd frequency, the path is pseudo-palindromic
                if odd_freq_count <= 1:
                    return 1
                else:
                    return 0

            # Traverse left and right subtrees
            left_count = dfs(node.left, freq)
            right_count = dfs(node.right, freq)

            # Backtrack: decrease the frequency of the current node's value
            freq[node.val] -= 1

            # Return the total count of pseudo-palindromic paths found so far
            return left_count + right_count

        return dfs(root, [0] * 10)