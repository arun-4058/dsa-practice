# find the nth ugly number
# an ugly number has prime factors limited to 2,3,5


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]*n
        idx2 = idx3 = idx5 = 0

        for i in range(1, n):
            next_ugly = min(ugly[idx2]*2, ugly[idx3]*3, ugly[idx5]*5)
            ugly[i] = next_ugly

            if next_ugly == ugly[idx2]*2:
                idx2 += 1
            if next_ugly == ugly[idx3]*3:
                idx3 += 1
            if next_ugly == ugly[idx5]*5:
                idx5 += 1
        return ugly[-1]