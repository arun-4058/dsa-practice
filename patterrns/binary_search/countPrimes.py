# count all primes strictly less than n


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False

        for idx in range(2, n + 1):
            if primes[idx]:
                i = 2
                while i * idx <= n:
                    primes[i * idx] = False
                    i += 1
        prime_count = 0
        for idx, value in enumerate(primes):
            if idx < n and value:
                prime_count += 1
        return prime_count



