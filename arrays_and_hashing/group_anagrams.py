from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_str = []
        for s in strs:
            sorted_str.append(sorted(s))
        groups = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]
        res = []
        for group in groups.values():
            res.append(group)
        return res
    
    # this implementation will fail for the case : ["bdddddddddd","bbbbbbbbbbc"]
    def groupAnagramsOptimized(self, strs):
        def getKey(s):
            f = [0]*26
            for c in s:
                f[ord(c) - ord('a')]+=1
            return ''.join([str(i) for i in f])
        
        groups = {}
        for s in strs:
            k = getKey(s)
            groups[k] = groups.get(k, []).append(s)
        return groups.values()

    # instead of using concatenated freq as keys use the list as key
    def groupAnagramsOptimized1(self, strs):
        ans = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')]+=1
            ans[tuple(freq)].append(s)
        return ans.values()

sol = Solution()
str = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(str))
print(sol.groupAnagramsOptimized1(str))