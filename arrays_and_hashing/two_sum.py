class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in m:
                return [m[diff], i]
            m[nums[i]] = i
        return [-1, -1]
    
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([2,7,11,15], 30))