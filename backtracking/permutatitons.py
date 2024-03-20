from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ds = []
        freq = [0]*len(nums)

        def recur_permute(arr: List[int], freq: List[int]):
            if len(ds) == len(arr):
                res.append(ds.copy())
                return

            for i in range(len(arr)):
                if not freq[i]:
                    ds.append(arr[i])
                    freq[i] = 1
                    recur_permute(arr, freq)
                    freq[i] = 0
                    ds.pop()

        recur_permute(nums, freq)
        return res

