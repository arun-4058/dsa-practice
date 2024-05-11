from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    lcp = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return lcp
        lcp += strs[0][i]
    return lcp
