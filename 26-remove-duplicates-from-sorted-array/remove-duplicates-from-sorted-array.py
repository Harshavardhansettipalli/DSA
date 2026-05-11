class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j =1
        uniq = 1
        while(j < len(nums)):
            if (nums[i] == nums[j]):
                j+=1
                continue
            nums[i+1] = nums[j]
            i+=1
            uniq+=1
        return uniq
        
        