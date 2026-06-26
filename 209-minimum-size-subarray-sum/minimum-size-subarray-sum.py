class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        res = float('inf')
        low = 0
        high = 0
        for high in range(len(nums)):
            sum += nums[high]
            while(sum >= target):
                length = high - low + 1
                res = min(length, res)
                sum -= nums[low]
                low += 1
        return res if res != float('inf') else 0
        