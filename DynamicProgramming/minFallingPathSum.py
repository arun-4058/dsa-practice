
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [ [101 for _ in range(cols)] for _ in range(rows)]

        for i in range(cols):
            dp[0][i] = matrix[0][i]

        for r in range(1, rows):
            for c in range(0, cols):
                if c == 0:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c+1])
                elif c == cols-1:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c-1])
                else:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c-1], dp[r-1][c+1])
        return min(dp[rows-1])
