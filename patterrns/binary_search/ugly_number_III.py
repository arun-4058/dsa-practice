# An ugly number is a positive integer that is divisible by a, b, or c.
# Given four integers n, a, b, and c, return the nth ugly number.
import math


class Solution:
    # MLE : 1 <= n, a, b, c <= 109 : 1 <= a * b * c <= 1018
    def nthUglyNumberMLE(self, n: int, a: int, b: int, c: int) -> int:
        ugly = [1]*n
        idxa = idxb = idxc = 1

        for i in range(n):
            next_ugly = min(idxa*a, idxb*b, idxc*c)
            ugly[i] = next_ugly

            if next_ugly == idxa*a:
                idxa += 1
            if next_ugly == idxb*b:
                idxb += 1
            if next_ugly == idxc*c:
                idxc += 1
        return ugly[-1]

    # solution using binary search
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def enough(num: int) -> bool:
            total = num // a + num // b + num // c - num // ab - num // bc - num // ca + num // abc
            return total >= n

        ab = a * b // math.gcd(a, b)
        bc = b * c // math.gcd(b, c)
        ca = c * a // math.gcd(c, a)
        abc = a * bc // math.gcd(a, bc)

        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
