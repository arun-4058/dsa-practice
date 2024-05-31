def lengthOfLastWord(self, s: str) -> int:
    max_length = 0
    i, j = 0, 0

    while i < len(s) and j < len(s):
        while j < len(s) and s[j] != ' ':
            j += 1
        max_length = max(max_length, (j - i))
        while j < len(s) and s[j] == ' ':
            j += 1
        i = j
    return max_length