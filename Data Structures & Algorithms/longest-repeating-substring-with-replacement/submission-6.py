from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = defaultdict(int)
        mx = 0
        for r, ch in enumerate(s):
            mp[ch] += 1
            n = r - l + 1
            if (n - max(mp.values())) > k:
                mp[s[l]] -= 1
                l += 1
            n = r - l + 1
            mx = max(mx, n)
        return mx

