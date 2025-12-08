import array
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        harsha = int("".join(map(str, digits)))
        vardhan  = harsha + 1
        vishnu  = list(map(int,str(vardhan)))
        return vishnu


        