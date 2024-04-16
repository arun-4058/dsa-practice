class Solution:
    def numSquares(self, n: int) -> int:
        def getPerfectSquares(n: int) -> List[int]:
            res = []
            i = 1
            while i*i <= n:
                res.append(i*i)
                i+=1
            return res
        perfect_squares = getPerfectSquares(n)

        dp = [n+1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n+1):
            for ps in perfect_squares:
                if ps<=i:
                    dp[i] = min(dp[i], dp[i-ps]+1)
        return dp[n]
