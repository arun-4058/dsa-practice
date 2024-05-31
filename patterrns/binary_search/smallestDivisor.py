# Given an array of integers nums and an integer threshold,
# we will choose a positive integer divisor, divide all the array by it, and sum the division's result.
# Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element.
# (For example: 7/3 = 3 and 10/2 = 5).
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(divisor: int) -> bool:
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

