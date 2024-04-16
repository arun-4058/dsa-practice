# Nearly everyone has used the Multiplication Table.
# The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def enough(num: int) -> bool:
            count = 0
            for val in range(1, m + 1):
                add = min(num // val, n)
                if add == 0:
                    break
                count += add
            return count >= k

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left