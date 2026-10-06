class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        mx = 0
        for r, ch in enumerate(s):
            if ch in mp:
                l = max(l, mp[ch] + 1)
            mx = max(mx, r - l + 1)
            mp[ch] = r
        return mx 