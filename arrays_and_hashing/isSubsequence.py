# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).
# Follow UP: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


# time complexity :: O(n)
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# for the case when there are 10^9 s and need to check for every s if it's a substring of t or not
def isSubsequenceOptimized(s: str, t: str) -> bool:
    index = {}
    for i, c in enumerate(t):
        if c not in index:
            index[c] = []
        index[c].append(i)

    prev_pos = -1
    for c in s:
        if c not in index:
            return False

        # find the position of the char greater than pre_position
        position = index[c]
        left, right = 0, len(position)-1
        while left <= right:
            mid = left + (right - left) // 2
            if position[mid] <= prev_pos:
                left = mid + 1
            else:
                right = mid - 1

        # if no position found greater than the prev_pos
        if left == len(position):
            return False

        # update prev_pos to the found position
        prev_pos = left

    return True
