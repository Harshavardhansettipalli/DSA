class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = defaultdict(int)
        low = 0
        high = 0
        res = 0
        n = len(s)
        for high in range(n):
            f[s[high]] += 1
            maxi = max(f.values())
            length = high - low + 1
            diff = length - maxi
            while(diff > k):
                f[s[low]] -= 1
                low += 1
                if(f[s[low]] == 0):
                    del f[s[low]]
                maxi = max(f.values())
                length = high - low +1
                diff = length -maxi
            res = max(res, length)
        return res 
        