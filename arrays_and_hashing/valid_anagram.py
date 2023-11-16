# this problem can be solved using sorting and hashmaps
# idea is to check for the freq of each character and compare

class Solution(object):

    # sol 1:
    def isAnagramUsingSorting(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    
    # sol 2:
    def isAnagramUsingHashMap(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

    # sol 3:
    def isAnagramUsingSingleHashMap(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            counts[t[i]] = counts.get(t[i], 0) - 1

        for v in counts.values():
            if v != 0:
                return False
        return True

sol = Solution()

print("using sorting :: " + str(sol.isAnagramUsingSorting("anagram", "nagaram")))
print("using sorting :: " + str(sol.isAnagramUsingSorting("rat", "car")))

print("using hashmap :: " + str(sol.isAnagramUsingSorting("anagram", "nagaram")))
print("using hashmap :: " + str(sol.isAnagramUsingSorting("rat", "car")))

print("using single hashmap :: " + str(sol.isAnagramUsingSorting("anagram", "nagaram")))
print("using single hashmap :: " + str(sol.isAnagramUsingSorting("rat", "car")))