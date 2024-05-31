import heapq
from typing import List


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        idea is to get the frequency of each number, then bucket the numbers according to the frequency
        iterate the frequency bucket in reverse order to get the k frequent elements
        """
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(res) >= k:
                break
            if buckets[i]:
                res.extend(buckets[i])
        return res

        # res = []
        # for i in range(len(buckets) - 1, 0, -1):
        #     for n in buckets[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
        # return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq = []
        for n in nums:
            heapq.heappush(hq, n)
            if len(hq) > k:
                heapq.heappop(hq)
        return hq


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))
