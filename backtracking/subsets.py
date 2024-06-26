# Given an integer array nums of unique elements,
# return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            dfs(i+1)
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res
