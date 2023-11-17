class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is not O(n) solution, will get TLE for n=10^9
        s = set(nums)
        res = 0
        for num in nums:
            start = num
            count = 0
            while start in s:
                count+=1
                start+=1
            res = max(res, count)
        return res

    def longestConsecutiveOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        # don't start counting until you get the start of the seq
        # in the above solution we are making every element as the start
        # so [100,4,200,1,3,2] for 3 -> 3,4, 2 -> 2,3,4 and 1 -> 1,2,3,4 
        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

sol = Solution()
nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))
print(sol.longestConsecutiveOptimized(nums2))