class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a , b , c = [] , [] , []
        i = j = index = 0
        for x in nums:
            if(x > 0):
                b.append(x*x)
            else:
                a.append(x*x)
        a.reverse()
        while( i < len(a) and j < len(b)):
            if(a[i] < b[j]):
                c.append(a[i])
                i+=1
                index+=1
            else:
                c.append(b[j])
                j+=1
                index+=1
        c.extend(a[i:])
        c.extend(b[j:])
        return c
        
        