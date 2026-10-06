from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key = Counter(s1)
        l = 0

        mp = Counter(s2[:len(s1)])
        if mp == key: return True
        for r in range(len(s1), len(s2)):
            mp[s2[r]] += 1
            mp[s2[l]] -= 1
            l += 1
            if mp == key: return True
        return False