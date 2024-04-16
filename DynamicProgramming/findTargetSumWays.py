class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            count_plus = dfs(index + 1, current_sum + nums[index])
            count_minus = dfs(index + 1, current_sum - nums[index])
            memo[(index, current_sum)] = count_plus + count_minus
            return memo[(index, current_sum)]

        return dfs(0, 0)
