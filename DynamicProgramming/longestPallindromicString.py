from functools import lru_cache


class Solution:
    # returns length of the longest palindromic string
    def longestPalindrome(self, s: str) -> int:
        @lru_cache(None)
        def lps(x, i, j) -> int:
            if i == j:
                return 1
            if x[i] == x[j] and i + 1 == j:
                return 2
            if x[i] == x[j]:
                return lps(x, i + 1, j - 1) + 2
            if x[i] != x[j]:
                return max(lps(x, i + 1, j), lps(x, i, j - 1))
        return lps(s, 0, len(s) - 1)



