from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search_left(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def search_right(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = search_left(nums, target)
        right_idx = search_right(nums, target)

        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]

