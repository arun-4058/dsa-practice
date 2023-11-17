class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l+=1
            elif numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            else:
                l+=1
                r-=1
        return [-1, -1]

numbers = [2,7,11,15]
target = 17
sol = Solution()
print(sol.twoSum(numbers, target))