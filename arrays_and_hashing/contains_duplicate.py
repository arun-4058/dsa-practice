from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sol = Solution()
print(sol.containsDuplicate(a))
print(sol.containsDuplicate(b))
