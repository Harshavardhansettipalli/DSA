class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hello = {}
        for i in nums:
            if i not in hello :
                hello[i] = 1
            else:
                return True
                
                
        return False
                
        