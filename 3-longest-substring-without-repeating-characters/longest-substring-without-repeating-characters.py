class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        low = 0
        res = 0
        for high in range(len(s)):
            freq[s[high]] += 1
            while(len(freq) < (high - low + 1)):
                freq[s[low]] -= 1
                if(freq[s[low]] == 0):
                    del freq[s[low]]
                low += 1
            length = high - low  + 1
            res = max(res, length)
        return res
        