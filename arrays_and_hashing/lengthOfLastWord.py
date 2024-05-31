def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    j = i
    while j >= 0 and s[j] != ' ':
        j -= 1
    return i - j


def lengthOfLastWordOptimized(self, s: str) -> int:
    c = 0
    for i in s[::-1]:
        if i == " ":
            if c >= 1:
                return c
        else:
            c += 1
    return c
