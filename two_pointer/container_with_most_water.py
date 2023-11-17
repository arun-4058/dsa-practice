class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        res = 0

        while i < j:
            res = max(res, min(height[i], height[j])*(j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))