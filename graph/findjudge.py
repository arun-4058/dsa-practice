class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming, outgoing = [0] * (n + 1), [0] * (n + 1)

        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        return -1
