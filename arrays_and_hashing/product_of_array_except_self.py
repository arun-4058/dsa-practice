class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # a = [1,2,3,4]    sol = [24,12,8,6]
        # l = [1,1,2,6]
        # r = [24,12,4,1]#
        lp,rp = [1]*len(nums), [1]*len(nums)
        lp[0] = 1
        rp[len(nums)-1] = 1
        p = 1
        for i in range(len(nums)-1):
            lp[i+1] = p*nums[i]
            p = lp[i+1]
        p = 1
        for i in range(len(nums)-2, -1, -1):
            rp[i] = p*nums[i+1]
            p = rp[i]
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = lp[i]*rp[i]
        return res

    def productExceptSelf1(self, nums):
        # a = [1,2,3,4]
        # res = [1, 1, 2, 6]
        # postfix = 1
        # res = [24, 12, 8, 6]
        # postfix 4, 12, 24
        # #
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
print(sol.productExceptSelf1(nums))