class Solution:
    def valid(self, tmap, smap):
        for ch in tmap:
            if smap[ch] < tmap[ch]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for ch in t:
            tmap[ch] += 1
        low = 0
        start = -1
        res = float('inf')
        for high in range(len(s)):
            smap[s[high]] += 1
            while self.valid(tmap,smap):
                length = high - low + 1
                if length < res:
                    res = length
                    start = low
                smap[s[low]] -= 1
                low += 1
        if start == -1:
            return ""
        return s[start:start+res]