class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        memo = {}

        def dfs(index, current_sum):
            if current_sum == target_sum:
                return True
            if current_sum > target_sum or index >= len(nums):
                return False
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            if dfs(index + 1, current_sum + nums[index]):
                memo[(index, current_sum)] = True
                return True
            if dfs(index + 1, current_sum):
                memo[(index + 1, current_sum)] = True
                return True
            memo[(index, current_sum)] = False
            return False

        return dfs(0, 0)