class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_max = Max = sum(nums[:k])
        for i in range(k, len(nums)):
            cur_max += nums[i] - nums[i-k]
            Max = max(cur_max, Max)
        return Max/k
        