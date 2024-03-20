# Given an integer array nums that may contain duplicates,
# return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, subset: List[int]):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res
