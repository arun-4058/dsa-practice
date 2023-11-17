class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = [0]*len(height), [0]*len(height)
        mx = 0

        for i in range(len(height)):
            mx = max(height[i], mx)
            l[i] = mx
        
        mx = 0
        for i in range(len(height)-1, -1, -1):
            mx = max(height[i], mx)
            r[i] = mx
        
        d = [min(l[i], r[i]) - height[i] for i in range(len(height))]
        res = 0
        for i in d:
            res += i
        return res

    def trapTwoPointers(self, height):
        if not height:
            return 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res
        

sol = Solution()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]  #[4,2,0,3,2,5]
print(sol.trap(heights))
print(sol.trapTwoPointers(heights))